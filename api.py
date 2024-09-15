from flask import Flask, make_response, send_file, jsonify
import json
import threading
import os
from call import make_call, wait_for_prompt, process_transcript, follow_up, _synthesize_follow_up, _generate_pdf, setup_app

app = Flask(__name__)

TWILIO_PHONE_NUMBER = os.getenv('TWILIO_PHONE_NUMBER')

setup_app(app)

@app.route("/patientpdf/<patientID>/startcall", methods=["GET"])
def start_call(patientID=None):
    with open("data/patients/patients.json", "r") as f:
        data = json.load(f)
        data = {patient['id']: patient for patient in data}

    if patientID is None or patientID not in data:
        return make_response("Patient not found", 404)
    
    patient = data[patientID]

    threading.Thread(target=make_call, args=(
        TWILIO_PHONE_NUMBER,
        patient['number'],
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
            (_generate_pdf, (f'out/{patientID}.pdf', patient['name'], patient['age'], patient['sex']))
        ]
    )).start()

    return jsonify({"status": "success"})

@app.route("/patientpdf/<patientID>", methods=["GET"])
def get_pdf(patientID=None):
    if patientID is not None:
        path = f"out/{patientID}.pdf"
        return send_file(path, as_attachment=False)

@app.route("/userdata", methods=["GET"])
def get_user_data():
    with open("data/patients/patients.json", "r") as f:
        data = json.load(f)
        return jsonify(data)

@app.route("/createaccount", methods=["POST"])
def create_account():
    pass

if __name__ == '__main__':
    app.run(port=8080, host='0.0.0.0')
