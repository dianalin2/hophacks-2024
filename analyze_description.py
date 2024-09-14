import csv

symptoms = []

def collect_symptoms_data():
    with open('symptom_severity.csv','r') as csv_file:
        reader =  csv.reader(csv_file)

        for row in reader:
            symptoms.append(row[0])
        csv_file.close()
        
    symptoms.remove(symptoms[0])
    
collect_symptoms_data()
print(symptoms)

def symptom_lookup(word):
    if word in symptoms:
        return word
    else:
        return None




