from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say
from uuid import uuid4
from flask import Flask, request, send_from_directory, redirect
import threading
from main import process
from follow_up import synthesize_follow_up
import os

app = Flask(__name__)

current_calls = {}

TWILIO_ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
BASE_URL = os.getenv('BASE_URL')
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

@app.route('/gather/callback', methods=['POST'])
def gather_callback():
    sid = request.form['CallSid']
    speech_result = request.form['SpeechResult']
    return current_calls[sid]['callback'](sid, speech_result)

@app.route('/xml/<filename>', methods=['GET'])
def get_xml(filename):
    return send_from_directory('xml', filename)

def upload_xml(content, filename):
    with open(f'xml/{filename}', 'w') as f:
        f.write(content)

    return f'/xml/{filename}'

def generate_id():
    return str(uuid4())

def make_call(from_, to, initial_text, nexts):
    next_file = f'{generate_id()}.xml'
    response = VoiceResponse()
    response.say(initial_text)
    response.pause(length=1)
    response.redirect(f'/xml/{next_file}', method='GET')

    curr_id = generate_id()
    curr_url = upload_xml(str(response), f'{curr_id}.xml')

    call = client.calls.create(
        from_=from_,
        to=to,
        url=f'{BASE_URL}{curr_url}',
        method='GET'
    )

    current_calls[call.sid] = {
        'from': from_,
        'to': to,
        'curr_url': curr_url,
        'next_file': next_file,
        'callback': None,
        'next': nexts,
        'all_responses': [],
        'follow_ups': [],
        'info': []
    }

    if not current_calls[call.sid]['next']:
        return goodbye(call.sid)

    next, current_calls[call.sid]['next'] = current_calls[call.sid]['next'][0], current_calls[call.sid]['next'][1:]
    next[0](call.sid, *next[1])

    return call.sid

def generate_voice_response(sid, text):
    next_file = f'{generate_id()}.xml'
    response = VoiceResponse()
    response.say(text)
    response.pause(length=1)
    response.redirect(f'/xml/{next_file}', method='GET')

    curr_id = current_calls[sid]['next_file']
    current_calls[sid]['curr_url'] = upload_xml(str(response), f'{curr_id}')
    current_calls[sid]['next_file'] = next_file

    if not current_calls[sid]['next']:
        goodbye(sid)
        return current_calls[sid]['curr_url']
    
    curr_url = current_calls[sid]['curr_url']

    next, current_calls[sid]['next'] = current_calls[sid]['next'][0], current_calls[sid]['next'][1:]
    next[0](sid, *next[1])

    return curr_url

def goodbye(sid):
    response = VoiceResponse()
    response.say('Thank you for your time. A doctor will be with you shortly.')
    response.hangup()

    return upload_xml(str(response), f'{current_calls[sid]["next_file"]}')

def gather_response(sid, speech_result):
    current_calls[sid]['all_responses'].append(speech_result)

    if not current_calls[sid]['next']:
        return redirect(goodbye(sid))

    next, current_calls[sid]['next'] = current_calls[sid]['next'][0], current_calls[sid]['next'][1:]
    return redirect(next[0](sid, *next[1]))

def wait_for_prompt(sid):
    next_file = f'{generate_id()}.xml'

    response = VoiceResponse()
    response.gather(input='speech', action='/gather/callback', method='POST')
    response.say('You did not respond to the prompt. Goodbye.')

    curr_id = current_calls[sid]['next_file']
    current_calls[sid]['next_file'] = next_file
    current_calls[sid]['callback'] = gather_response
    current_calls[sid]['curr_url'] = upload_xml(str(response), f'{curr_id}')

    return current_calls[sid]['curr_url']

def process_transcript(sid):
    transcript = current_calls[sid]['all_responses'][-1]
    info = process(transcript)
    current_calls[sid]['info'].append(info)

    if not current_calls[sid]['next']:
        return goodbye(sid)
    
    next, current_calls[sid]['next'] = current_calls[sid]['next'][0], current_calls[sid]['next'][1:]
    return next[0](sid, *next[1])

def _synthesize_follow_up(sid):
    symptoms = current_calls[sid]['info'][-1][1]
    follow_up_questions = synthesize_follow_up(symptoms)
    current_calls[sid]['follow_ups'] = follow_up_questions

    next, current_calls[sid]['next'] = current_calls[sid]['next'][0], current_calls[sid]['next'][1:]
    return next[0](sid, *next[1])

def follow_up(sid, question_num):
    return generate_voice_response(sid, current_calls[sid]['follow_ups'][question_num])

if __name__ == '__main__':
    threading.Thread(target=make_call, args=(
        '+18333685475',
        '+12404531668',
        'Hello! You have reached Wahoowa. Can you please describe what symptoms you have been experiencing recently?',
        [
            (wait_for_prompt, ()),
            (process_transcript, ()),
            (_synthesize_follow_up, ()),
            (follow_up, (0,)),
            (wait_for_prompt, ()),
            (process_transcript, ()),
            (follow_up, (1,)),
            (wait_for_prompt, ()),
            (process_transcript, ()),
        ]
    )).start()

    app.run(port=8080, host='0.0.0.0')
