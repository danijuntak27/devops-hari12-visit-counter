from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis',port=6379)

@app.route ("/")
def hello():
    try:
        visits = cache.incr('counter')
        return f"Hello! This page has been visited {visits} times."
    except redis.exception.ConnectionError:
        return "Redis is not reachable!"