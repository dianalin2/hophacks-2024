import csv
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
import pickle

# nltk.download()

symptoms = []
patient_symptoms = []

def collect_symptoms_data():
    with open('data/symptom_severity.csv','r') as csv_file:
        reader =  csv.reader(csv_file)

        for row in reader:
            symptoms.append(row[0])
            symptoms[-1] = symptoms[-1].replace("_"," ")
        csv_file.close()
    symptoms.remove(symptoms[0])

def collect_symptoms_synonyms():
    with open('data/symptoms_synonyms.pkl', 'rb') as f:
        symptoms_synonyms_raw = pickle.load(f)
        symptoms_synonyms = {}
        for key in symptoms_synonyms_raw.keys():
            for synonym in symptoms_synonyms_raw[key]:
                symptoms_synonyms[synonym.lower()] = key.lower()
        print(symptoms_synonyms)
        return symptoms_synonyms
symptoms_synonyms = collect_symptoms_synonyms()
# print(symptoms_synonyms)

def collect_word_families():
    with open('data/word_families.pkl', 'rb') as f:
        word_families = pickle.load(f)
        return word_families
word_info = collect_word_families()
word_representative = word_info[0]
word_families = word_info[1]

# analyze transcript returns a dictionary with the potential symptom as well as how many synonyms were detected
allowed_POS = ['NNP', 'VBG', 'JJ', 'NN', 'NNS', 'VBP', 'VBD', 'CC', 'RB', 'VBN', 'DT', 'JJS', 'CD']
def analyze_transcript(transcript):
    tokenized = sent_tokenize(transcript)
    potential_symptoms = {}
    for i in tokenized:
        wordsList = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(wordsList)
        for word in tagged:
            # if word[1] in allowed_POS:
            result = symptom_lookup(word[0])
            if result is not None:
                if result in potential_symptoms.keys():
                    potential_symptoms[result] += 1
                else:
                    potential_symptoms[result] = 1
    # delete = []
    # for key in potential_symptoms.keys():
    #     # condition for whether potential symptom is accepted
    #     if key.count(" ") + 1 > potential_symptoms[key]:
    #         delete.append(key)
    # for key in delete:
    #     del potential_symptoms[key]
    return potential_symptoms

def symptom_lookup(word):
    if word.lower() in symptoms:
        return word.lower()
    if word.lower() in symptoms_synonyms.keys():
        return symptoms_synonyms[word]
    elif word_representative[word.lower()] is not None:
        for family_member in word_families[word_representative[word.lower()]]:
            if family_member in symptoms_synonyms.keys():
                return symptoms_synonyms[family_member]
            elif family_member in symptoms:
                return family_member
    return None

# print(analyze_transcript("These days I feel a lot of fatigue."))


print(symptom_lookup("puke"))

