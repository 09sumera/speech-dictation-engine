from faster_whisper import WhisperModel

model = None

def get_model():
    global model
    if model is None:
        model = WhisperModel("tiny", device="cpu")
    return model

def transcribe_audio(file_path):
    model = get_model()
    segments, info = model.transcribe(file_path)
    text = " ".join([segment.text for segment in segments])
    return text