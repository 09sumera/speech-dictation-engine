import os
import requests

def transcribe_audio(filepath):

    api_key = os.getenv("DEEPGRAM_API_KEY")

    url = "https://api.deepgram.com/v1/listen"

    headers = {
        "Authorization": f"Token {api_key}",
        "Content-Type": "audio/wav"
    }

    with open(filepath, "rb") as audio:
        response = requests.post(url, headers=headers, data=audio)

    result = response.json()

    transcript = result["results"]["channels"][0]["alternatives"][0]["transcript"]

    return transcript