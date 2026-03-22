from flask import Flask, render_template, request, jsonify, Response
from bson import ObjectId
from stt_engine import transcribe_audio
from pipeline import process_text
from db import collection
import os

app = Flask(__name__)

# -------------------------------
# Upload folder setup
# -------------------------------
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# -------------------------------
# Home Page
# -------------------------------
@app.route("/")
def home():
    return render_template("index.html")


# -------------------------------
# Process live speech text
# -------------------------------
@app.route("/process_text", methods=["POST"])
def process_live_text():

    data = request.get_json()

    raw_text = data.get("text", "")

    if raw_text.strip() == "":
        return jsonify({"cleaned": ""})

    clean_text = process_text(raw_text, "formal")

    try:
        collection.insert_one({
            "raw_text": raw_text,
            "clean_text": clean_text
        })
    except Exception as e:
        print("MongoDB Error:", e)

    return jsonify({"cleaned": clean_text})


# -------------------------------
# Upload audio file
# -------------------------------
@app.route("/upload", methods=["POST"])
def upload():

    if "audio" not in request.files:
        return "No audio file provided"

    audio = request.files["audio"]

    if audio.filename == "":
        return "Empty file"

    filepath = os.path.join(UPLOAD_FOLDER, audio.filename)
    audio.save(filepath)

    raw_text = transcribe_audio(filepath)

    clean_text = process_text(raw_text, "formal")

    try:
        collection.insert_one({
            "raw_text": raw_text,
            "clean_text": clean_text
        })
    except Exception as e:
        print("MongoDB Error:", e)

    return render_template(
        "index.html",
        raw=raw_text,
        clean=clean_text
    )


# -------------------------------
# Transcript History Page
# -------------------------------
@app.route("/history")
def history():

    transcripts = list(collection.find().sort("_id", -1))

    return render_template(
        "history.html",
        transcripts=transcripts
    )


# -------------------------------
# Download transcript
# -------------------------------
@app.route("/download/<id>")
def download(id):

    transcript = collection.find_one({"_id": ObjectId(id)})

    text = f"""
AI Speech Dictation Transcript

Raw Speech:
{transcript['raw_text']}

Clean Text:
{transcript['clean_text']}
"""

    return Response(
        text,
        mimetype="text/plain",
        headers={
            "Content-Disposition": "attachment;filename=transcript.txt"
        }
    )

@app.route("/download/latest")
def download_latest():

    transcript = collection.find_one(sort=[("_id", -1)])

    if not transcript:
        return "No transcript available"

    text = f"""
AI Speech Dictation Transcript

Raw Speech:
{transcript['raw_text']}

Clean Text:
{transcript['clean_text']}
"""

    return Response(
        text,
        mimetype="text/plain",
        headers={
            "Content-Disposition": "attachment; filename=latest_transcript.txt"
        }
    )
@app.route("/search")
def search():

    query = request.args.get("q","")

    if query == "":
        transcripts = list(collection.find().sort("_id",-1))
    else:
        transcripts = list(collection.find({
            "$or":[
                {"raw_text":{"$regex":query,"$options":"i"}},
                {"clean_text":{"$regex":query,"$options":"i"}}
            ]
        }).sort("_id",-1))

    return render_template("history.html", transcripts=transcripts, search=query)
@app.route("/test")
def test():
    return "Server is running!"

# -------------------------------
# Run server
# -------------------------------
if __name__ == "__main__":
 port = int(os.environ.get("PORT", 5000))
 app.run(host="0.0.0.0", port=port)