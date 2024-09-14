import pickle
import re

with open('symptoms_synonyms_new.pkl', 'rb') as f:
    all_word_definitions = pickle.load(f)

all_word_definitions['bloody stool'] = ['Blood', 'Stool', 'Poop', 'Feces', 'Bloody']
all_word_definitions['continuous feel of urine'] = ['Always', 'Urine', 'Pee', 'Continuous', 'Urination']
all_word_definitions['yellow urine'] = ['Yellow', 'Urine', 'Pee', 'Color', 'Yellow Pee']
all_word_definitions['pus filled pimples'] = ['Pus', 'Filled', 'Pimples', 'Pimple', 'Pus Filled', 'Whitehead', 'Zit', 'Acne']
all_word_definitions['pain in anal region'] = ['Pain', 'Anal', 'Region', 'Butt', 'Rectum', 'Anus', 'Anal Pain']
all_word_definitions['receiving unsterile injections'] = ['Receiving', 'Sterile', 'Injections', 'Injection', 'Needle', 'Syringe', 'Vaccine', 'Shot', 'Sterile Injection', 'Unsafe', 'Safety']

for key, value in all_word_definitions.items():
    if type(value) is list:
        continue
    nvalue = re.findall(r'\*\*(\w+).?\*\*', value.text)
    nvalue += re.findall(r'"(\w+)"', value.text)
    nvalue += re.findall(r'\'(\w+)\'', value.text)
    nvalue += re.findall(r'\d. (\w+)', value.text)
    nvalue += re.findall(r'\d. \*\*(\w+).?\*\*', value.text)
    nvalue = list(set(nvalue))
    if nvalue:
        all_word_definitions[key] = nvalue
    else:
        x = re.findall(r'\d. \*\*((\w| )+).?\*\*', value.text)
        nvalue = [x[0] for x in x]
        print(key, value.text)
        print(nvalue)
        print('bad')
        all_word_definitions[key] = nvalue

print(all_word_definitions)
print(len(all_word_definitions))

with open('synonyms/symptoms_synonyms.pkl', 'wb') as f:
    pickle.dump(all_word_definitions, f)
