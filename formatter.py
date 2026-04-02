import requests

def correct_grammar(text):

    url = "https://api.languagetool.org/v2/check"

    data = {
        "text": text,
        "language": "en-US"
    }

    response = requests.post(url, data=data)
    result = response.json()

    corrected = text

    for match in result.get("matches", []):
        if match["replacements"]:
            replacement = match["replacements"][0]["value"]
            offset = match["offset"]
            length = match["length"]

            corrected = corrected[:offset] + replacement + corrected[offset+length:]

    return corrected