import spacy
# from spacy import displacy

text = "The patient presented with symptoms of fever and cough for the past week. A chest X-ray revealed bilateral pneumonia. A sputum culture was ordered to identify the cause of infection. Based on the clinical presentation and lab results, the patient was diagnosed with community-acquired pneumonia and prescribed a course of antibiotics. The physician also ordered a CT scan to evaluate for any possible complications and a blood test to check the patient's white blood cell count and liver function."

nlp = spacy.load("en_core_sci_lg")
doc = nlp(text)

# Print the original text
print(text)

# Iterate over the entities and print them
for ent in doc.ents:
    print(ent.text, ent.label_)
