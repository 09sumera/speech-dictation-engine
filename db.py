import os
from pymongo import MongoClient

mongo_uri = os.environ.get("MONGO_URI")

client = MongoClient(os.getenv("MONGO_URI"))

db = client["speech_db"]

collection = db["transcripts"]