import csv
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# nltk.download()

symptoms = ["fatigue"]
symptoms_common_words = {
    "tired": "fatigue",
    "scratchy": "itchy"
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

def symptom_lookup(word):
    if word in symptoms:
        return word
    else:
        for key in symptoms_common_words.keys():
            if word.lower() in key.lower():
                return symptoms_common_words[key]
        return None

allowed_POS = ['NNP', 'VBG', 'JJ', 'NN', 'NNS', 'VBP', 'VBD', 'CC', 'RB', 'VBN', 'DT', 'JJS', 'CD']
def analyze_transcript(transcript):
    tokenized = sent_tokenize(transcript)
    potential_symptoms = {}
    for i in tokenized:
        wordsList = nltk.word_tokenize(i)
        tagged = nltk.pos_tag(wordsList)
        for word in tagged:
            if word[1] in allowed_POS:
                result = symptom_lookup(word[0])
                if result is not None:
                    if result in potential_symptoms.keys():
                        potential_symptoms[result] += 1
                    else:
                        potential_symptoms[result] = 1
    delete = []
    for key in potential_symptoms.keys():
        # condition for whether potential symptom is accepted
        if key.count(" ") + 1 > potential_symptoms[key]:
            delete.append(key)
    for key in delete:
        del potential_symptoms[key]
    return potential_symptoms

print(analyze_transcript("I'm really tired these days."))




