from filler_removal import remove_fillers
from repetition_removal import remove_repetition
from formatter import correct_grammar
from tone_transformer import change_tone

def process_text(text, tone):

    text = remove_fillers(text)

    text = remove_repetition(text)

    text = correct_grammar(text)

    text = text.capitalize()

    text = change_tone(text, tone)

    return text