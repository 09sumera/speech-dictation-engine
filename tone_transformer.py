def change_tone(text, mode):

    if mode == "formal":
        text = text.replace("start", "begin")
        text = text.replace("get", "obtain")

    elif mode == "casual":
        text = text.replace("begin", "start")

    elif mode == "concise":
        text = text.replace("I think we should", "Let's")

    return text