import redis
import os
from dotenv import load_dotenv

load_dotenv()

def get_db():
    try:
        r = redis.Redis(
            host=os.getenv("KEYDB_HOST"),
            port=int(os.getenv("KEYDB_PORT")),
            password=os.getenv("KEYDB_PASSWORD"),
            decode_responses=True
        )
        r.ping()
        return r
    except redis.ConnectionError:
        print("Error de conexión con KeyDB")
        exit()
