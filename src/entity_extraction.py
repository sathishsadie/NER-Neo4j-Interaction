import spacy 
nlp = spacy.load('en_core_web_sm')
def extract_ner_entities(text):
    doc = nlp(text)
    entities = [{"text": ent.text, "label": ent.label_} for ent in doc.ents]
    return entities
