from pymongo import MongoClient

client = MongoClient("mongodb+srv://sumera0904_db_user:MHmbBNlunhfqQj2y@speech-dictation-cluste.3q5hteo.mongodb.net/?appName=speech-dictation-cluster")

db = client["speech_dictation"]

collection = db["transcripts"]