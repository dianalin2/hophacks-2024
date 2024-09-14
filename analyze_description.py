symptoms = []

def symptom_lookup(word):
    if word in symptoms:
        return word
    else:
        return None