import spacy

nlp = spacy.load("en_core_web_sm")

doc = nlp(open("test.plain", "r").read())

print([str(chunk) for chunk in doc.noun_chunks])
