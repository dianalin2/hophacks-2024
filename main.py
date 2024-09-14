from transcribe import start_transcribe
from analyze_description import analyze_transcript
from summarize import summarize
from diagnose import find_possible_diagnoses

def main():
    # tts prompt the user about how they are doing

    transcript = start_transcribe()
    info = process(transcript)
    print(info)

    # tts prompt ask follow up questions

    follow_up_transcript = start_transcribe()
    follow_up_info = process(follow_up_transcript)
    print(follow_up_info)
    
# pay attention to the order that this method returns the details
def process(transcript):
    symptoms = analyze_transcript(transcript)
    summary = summarize(transcript)
    diagnoses = find_possible_diagnoses(symptoms)

    return (summary, symptoms, diagnoses)

if __name__ == '__main__':
    main()

# The other day I was walking down the street and then I tripped on the sidewalk. After that I had a bruise on my knee and it hurt a lot.