from flask import Flask
import redis
import os

app = Flask(__name__)
redis_host = os.getenv("REDIS_HOST", "redis")
redis_client = redis.Redis(host=redis_host, port=6379, db=0)

@app.route('/')
def counter():
    count = redis_client.incr('hits')
    return f'Hallo! Diese Seite wurde {count} Mal aufgerufen.'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)