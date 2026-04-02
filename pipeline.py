from filler_removal import remove_fillers
from repetition_removal import remove_repetition
from formatter import correct_grammar
from tone_transformer import transform_tone

def process_text(text, tone):

    text = remove_fillers(text)

    text = remove_repetition(text)

    text = correct_grammar(text)

    text = text.capitalize()

    text = transform_tone(text, tone)

    return text