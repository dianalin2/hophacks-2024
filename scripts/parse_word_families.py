import pickle


word_families = {}
with open("data/word_families.txt", 'r') as file_object:
    line = file_object.readline()
    current_key = ""
    while line:
        if(not line[0].isspace()):
            current_key = line.strip()
            word_families[current_key] = []
        else:
            word_families[current_key].append(line.strip())
        line = file_object.readline()

#reorganize word families
word_representative = {}
for rep in word_families.keys():
    for family_member in word_families[rep]:
        word_representative[family_member] = rep

with open('data/word_families.pkl', 'wb') as f:
    pickle.dump((word_representative, word_families), f)

