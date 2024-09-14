import sys
import pickle
import google.generativeai as genai
import os

API_KEY = sys.argv[1]
DATASET_PATH = sys.argv[2]

genai.configure(api_key=API_KEY)

with open(DATASET_PATH, 'r') as f:
    lines = f.readlines()

all_symptoms = set()

for line in lines[1:]:
    symptoms = line.strip().split(',')[1:]
    for symptom in symptoms:
        symptom = symptom.strip().replace('_', ' ')
        if symptom:
            all_symptoms.add(symptom)

print(len(all_symptoms))

if os.path.exists('symptoms_synonyms.pkl'):
    with open('symptoms_synonyms.pkl', 'rb') as f:
        all_word_definitions = pickle.load(f)
else:
    all_word_definitions = {}

print(len(all_word_definitions))

for symptom in all_symptoms:
    if symptom in all_word_definitions:
        continue

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"Get ten common, unrelated, single words that are synonymous to the term '{symptom}'")
    print(response)
    all_word_definitions[symptom] = response.parts[0]
    print(symptom, all_word_definitions[symptom])
    print()

    with open('symptoms_synonyms_new.pkl', 'wb') as f:
        pickle.dump(all_word_definitions, f)
