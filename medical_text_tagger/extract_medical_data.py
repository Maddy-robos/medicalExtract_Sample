import spacy


def print_entities(text):
    nlp = spacy.load("en_ner_bc5cdr_md")
    doc = nlp(text)

    # Print the original text
    print(text)

    # Iterate over the entities and print them
    for ent in doc.ents:
        print(ent.text, ent.label_)

    nlp = spacy.load("en_core_med7_lg")
    doc = nlp(text)

    # Iterate over the entities and print them
    for ent in doc.ents:
        print(ent.text, ent.label_)


def extract_entities(text):
    nlp = spacy.load("en_ner_bc5cdr_md")
    doc = nlp(text)

    # Print the original text
    print(text)

    entities = []
    for ent in doc.ents:
        current_json = {}
        print(ent.text, ent.label_, '\n')

        if ent.label_ == 'DISEASE':
            current_json['type'] = 'diagnosis'
            current_json['value'] = ent.text
        elif ent.label_ == 'DRUG':
            current_json['type'] = 'prescription'
            current_json['value'] = ent.text
        elif ent.label_ == 'STRENGTH':
            current_json['type'] = 'strength'
            current_json['value'] = ent.text
        elif ent.label_ == 'FREQUENCY':
            current_json['type'] = 'frequency'
            current_json['value'] = ent.text
        elif ent.label_ == 'CHEMICAL':
            current_json['type'] = 'chemical'
            current_json['value'] = ent.text

        if len(current_json) > 0:
            entities.append(current_json)

    print(entities)

    nlp = spacy.load("en_core_med7_lg")
    doc = nlp(text)

    # Iterate over the entities and print them
    for ent in doc.ents:
        current_json = {}
        if ent.label_ == 'DISEASE':
            current_json['type'] = 'diagnosis'
            current_json['value'] = ent.text
        elif ent.label_ == 'DRUG':
            current_json['type'] = 'prescription'
            current_json['value'] = ent.text
        elif ent.label_ == 'STRENGTH':
            current_json['type'] = 'strength'
            current_json['value'] = ent.text
        elif ent.label_ == 'FREQUENCY':
            current_json['type'] = 'frequency'
            current_json['value'] = ent.text
        elif ent.label_ == 'CHEMICAL':
            current_json['type'] = 'chemical'
            current_json['value'] = ent.text

        if len(current_json) > 0:
            entities.append(current_json)

    return entities
