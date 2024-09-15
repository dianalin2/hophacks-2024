# from communicate import start_transcribe, tts
from analyze_description import analyze_transcript
from summarize import summarize
from diagnose import find_possible_diagnoses
from follow_up import synthesize_follow_up

def main():
    # tts prompt the user about how they are doing
    tts("Hello! You have reached Wahoowa. Can you please describe what symptoms you have been experiencing recently?")

    transcript = start_transcribe()
    info = process(transcript)
    print(info)

    # tts prompt ask follow up questions
    follow_up_questions = synthesize_follow_up(info[1])

    tts(follow_up_questions[0])
    follow_up_transcript1 = start_transcribe()
    follow_up_info1 = process(follow_up_transcript1)
    print(follow_up_info1)

    tts(follow_up_questions[1])
    follow_up_transcript2 = start_transcribe()
    follow_up_info2 = process(follow_up_transcript2)
    print(follow_up_info2)

    
# pay attention to the order that this method returns the details
def process(transcript):
    symptoms = analyze_transcript(transcript)
    summary = summarize(transcript)
    diagnoses = find_possible_diagnoses(symptoms)

    return (summary, symptoms, diagnoses)

if __name__ == '__main__':
    main()

# The other day I was walking down the street and then I tripped on the sidewalk. After that I had a bruise on my knee and it hurt a lot.
