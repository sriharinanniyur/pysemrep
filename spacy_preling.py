import spacy

nlp = spacy.load("en_core_web_sm")

def sentence_data(sentence):
    doc = nlp(sentence)
    
