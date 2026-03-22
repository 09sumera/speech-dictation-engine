import re

fillers = [
"uh", "uhh", "um", "umm", "like", "you know","Hmm"
]

def remove_fillers(text):

    pattern = r'\b(' + '|'.join(fillers) + r')\b'

    cleaned = re.sub(pattern, '', text, flags=re.IGNORECASE)

    cleaned = re.sub(r'\s+', ' ', cleaned).strip()

    return cleaned