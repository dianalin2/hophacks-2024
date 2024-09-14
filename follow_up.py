import google.generativeai as genai
import sys

API_KEY = sys.argv[1]
DATASET_PATH = sys.argv[2]

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def synthesize_follow_up(symptoms):
    genai.configure(api_key=API_KEY)

    model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        response = model.generate_content(f"Generate two open-ended questions that can be asked to a patient who has the following symptoms: {', '.join(symptoms)}. The questions should be designed to help the patient describe their symptoms in more detail. Separate the questions with a semicolon.")
        response = response.parts[0].split(';')
        return response
    except Exception as e:
        return None
