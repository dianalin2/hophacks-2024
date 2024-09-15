import google.generativeai as genai
import sys
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv('API_KEY')

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")


def synthesize_follow_up(symptoms):
    genai.configure(api_key=API_KEY)

    model = genai.GenerativeModel("gemini-1.5-flash")

    try:
        response = model.generate_content(f"Generate two open-ended questions that can be asked to a patient who has the following symptoms: {', '.join(symptoms)}. The questions should be designed to help the patient describe their symptoms in more detail. Separate the questions with a semicolon.")
        response = response.parts[0].text.split(';')
        response = [question.strip() for question in response]
        return response
    except Exception as e:
        print(e)
        return None
