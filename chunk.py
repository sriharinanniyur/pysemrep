import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp(open("test.plain", "r").read())

print([chunk for chunk in doc.noun_chunks])
