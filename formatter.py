from textblob import TextBlob

def correct_grammar(text):
    blob = TextBlob(text)
    return str(blob.correct())