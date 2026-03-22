from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://sumera0904_db_user:Rqkg393CROueRkVj@speech-dictation-cluster.3q5hteo.mongodb.net/?retryWrites=true&w=majority"
)

db = client["speech_dictation_db"]

collection = db["transcripts"]