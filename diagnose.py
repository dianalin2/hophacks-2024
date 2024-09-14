import csv
from analyze_description import analyze_transcript

disease = {}

def collect_disease_data():
    with open('data/dataset.csv','r') as csv_file:
        reader =  csv.reader(csv_file)

        x = True
        for row in reader:
            if (not x):
                search_string = row[0]

                if (search_string in disease.keys()):
                    # pass
                    for i in range(len(disease[search_string])):
                       search_string1 = disease[search_string][i]
                       if (not search_string1 in disease[search_string]):
                           disease[search_string].append(search_string1)
                else:
                    disease[search_string] = row[1:]

                for i in range(len(disease[search_string])):
                    disease[search_string][i] = disease[search_string][i].replace("_"," ")
                    disease[search_string][i] = disease[search_string][i].lstrip()
                
                disease[search_string] = [x for x in disease[search_string] if x.strip()]
            x = False
                   
        csv_file.close()
collect_disease_data()
# print(disease)
print("\n---------------------------------------------\n")

def organize_diagnose_data():
    diagnose_map = {}
    for key in disease.keys():
        for symptom in disease[key]:
            if symptom in diagnose_map.keys():
                diagnose_map[symptom].append(key)
            else:
                diagnose_map[symptom] = [key]
    return diagnose_map
diagnose_map = organize_diagnose_data()


def find_possible_diagnoses():
    symptoms = analyze_transcript("These days I feel a lot of fatigue. It is really hard to move my hands. I often trip, stagger and tumble")
    diagnoses = {}
    for symptom in symptoms.keys():
        for diagnose in diagnose_map[symptom]:
            if diagnose in diagnoses.keys():
                diagnoses[diagnose] += symptoms[symptom]
            else:
                diagnoses[diagnose] = symptoms[symptom]
    print(diagnoses)
    diagnoses = sorted(diagnoses.items(), key=lambda x:x[1], reverse=True)
    return diagnoses
find_possible_diagnoses()