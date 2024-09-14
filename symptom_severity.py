import csv

severity = {}

def collect_severity_data():
    with open('data/symptom_severity.csv','r') as csv_file:
        reader =  csv.reader(csv_file)

        x = True
        for row in reader:
            if (not x):
                key = row[0].replace("_", " ")
                severity[key] = int(row[1])
            x = False
                   
        csv_file.close()

collect_severity_data()
print(severity)
