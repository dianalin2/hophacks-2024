import csv
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download()

symptoms = []
symptoms_common_words = {
    "fatigue": "tired",
    "itchy": "scratchy"
}
patient_symptoms = []

def collect_symptoms_data():
    with open('data/symptom_severity.csv','r') as csv_file:
        reader =  csv.reader(csv_file)

        for row in reader:
            symptoms.append(row[0])
            symptoms[-1] = symptoms[-1].replace("_"," ")
        csv_file.close()

    symptoms.remove(symptoms[0])
    
# collect_symptoms_data()
# print(symptoms)

allowed_POS = ["VBZ"]
def analyze_transcript(transcript):
    tokenized = sent_tokenize(transcript)
    for i in tokenized:
        wordsList = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(wordsList)
        for word in tagged:
            if word[1] in allowed_POS:
                print(word[0])

txt = "Sukanya, Rajib and Naba are my good friends. " \
    "Sukanya is getting married next year. " \
    "Marriage is a big step in one’s life." \
    "It is both exciting and frightening. " \
    "But friendship is a sacred bond between people." \
    "It is a special kind of love between us. " \
    "Many of you must have tried searching for a friend "\
    "but never found the right one."
analyze_transcript(txt)
    


collect_symptoms_data()
print(symptoms)

def symptom_lookup(word):
    if word in symptoms:
        return word
    else:
        for symptom in symptoms:
            for common in symptoms_common_words[symptom]:
                if common.lower() == word.lower():
                    patient_symptoms.append(symptom)
                    return symptom
        return None




