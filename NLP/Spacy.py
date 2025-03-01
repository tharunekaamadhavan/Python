import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Process the text
doc = nlp("Magna is studying at Saranathan College of Engineering.")

# Print recognized named entities
for ent in doc.ents:
    print(ent.text, "|", ent.label_)

# Display entities (Optional)
spacy.displacy.render(doc, style="ent", jupyter=True)
