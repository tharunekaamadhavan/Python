import spacy

# Load the en_core_web_sm model to get its path
nlp = spacy.load("en_core_web_sm")

# Print the path to the model directory
print(nlp.meta["path"])
