import re

def transform_tone(text, tone):

    tone = tone.lower().strip()

    # -----------------------
    # Formal tone
    # -----------------------
    if tone == "formal":

        replacements = {
            r"\bcan't\b": "cannot",
            r"\bwon't\b": "will not",
            r"\bi'm\b": "I am",
            r"\bit's\b": "it is",
            r"\bdon't\b": "do not"
        }

        for pattern, replacement in replacements.items():
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)

        text = "Kindly note that " + text


    # -----------------------
    # Casual tone
    # -----------------------
    elif tone == "casual":

        replacements = {
            r"\bcannot\b": "can't",
            r"\bwill not\b": "won't",
            r"\bi am\b": "I'm",
            r"\bit is\b": "it's",
            r"\bdo not\b": "don't"
        }

        for pattern, replacement in replacements.items():
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)


    # -----------------------
    # Neutral tone
    # -----------------------
    elif tone == "neutral":

        return text


    # -----------------------
    # Concise tone
    # -----------------------
    elif tone == "concise":

        text = text.lower()

        replacements = {
            r"i was wondering if you could": "please",
            r"could you please": "please",
            r"can you please": "please",
            r"i would like you to": "",
            r"i would appreciate if you could": "please",
            r"kindly": "",
            r"basically": "",
            r"actually": "",
            r"really": ""
        }

        for phrase, replacement in replacements.items():
            text = re.sub(phrase, replacement, text, flags=re.IGNORECASE)

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text).strip()

        # Capitalize sentence
        text = text.capitalize()

        if not text.endswith("."):
            text += "."


    # -----------------------
    # Professional tone
    # -----------------------
    elif tone == "professional":

        text = "This statement indicates that " + text


    # -----------------------
    # Email tone
    # -----------------------
    elif tone in ["email style", "email", "email-style"]:

        text = (
            "Dear Sir/Madam,\n\n"
            + text +
            "\n\nBest regards,\nAI Dictation System"
        )

    return text