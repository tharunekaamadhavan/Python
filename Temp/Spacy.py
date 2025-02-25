import spacy
nlp = spacy.load("en_core_web_sm")
doc=nlp("Dinesh is working at saranathan college of engineering")
for i in doc.ents:
    print(i.text,"|",i.label_)
