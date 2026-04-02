import os
from deepgram import DeepgramClient, PrerecordedOptions

def transcribe_audio(filepath):

    deepgram = DeepgramClient(os.getenv("DEEPGRAM_API_KEY"))

    with open(filepath, "rb") as audio:
        buffer_data = audio.read()

    options = PrerecordedOptions(
        model="nova-2",
        smart_format=True
    )

    response = deepgram.listen.prerecorded.v("1").transcribe_file(
        {"buffer": buffer_data},
        options
    )

    transcript = response["results"]["channels"][0]["alternatives"][0]["transcript"]

    return transcript