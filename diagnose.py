import csv

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
                
                disease[search_string] = [x for x in disease[search_string] if x.strip()]
            x = False
                   
        csv_file.close()

collect_disease_data()
print(disease)
