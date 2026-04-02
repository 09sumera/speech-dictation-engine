import re

def remove_fillers(text):

    fillers = [
        "um", "uh", "you know", "like", "actually",
        "basically", "literally", "i mean"
    ]

    for f in fillers:
        text = re.sub(rf"\b{f}\b", "", text, flags=re.IGNORECASE)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def remove_repetition(text):

    words = text.split()

    clean = []

    for word in words:
        if len(clean) == 0 or clean[-1] != word:
            clean.append(word)

    return " ".join(clean)