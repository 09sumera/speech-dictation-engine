def remove_repetition(text):

    words = text.split()

    cleaned = []

    for word in words:
        if not cleaned or cleaned[-1].lower() != word.lower():
            cleaned.append(word)

    return " ".join(cleaned)