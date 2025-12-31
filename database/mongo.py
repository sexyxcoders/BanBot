from pymongo import MongoClient

_client = None
_db = None

def init_db(mongo_uri: str, db_name: str):
    global _client, _db
    _client = MongoClient(mongo_uri)
    _db = _client[db_name]
    print("✅ MongoDB connected")

def get_db():
    if _db is None:
        raise RuntimeError("❌ Database not initialized")
    return _db