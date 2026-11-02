import os
from flask import Flask, jsonify
import redis

app = Flask(__name__)

redis_client = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)


@app.route("/")
def home():
    return "Welcome to DevOps Mastery Challenge!"


@app.route("/health")
def health():
    return jsonify({"status": "UP"})


@app.route("/api/info")
def api_info():
    return jsonify({
        "project": "DevOps Mastery Challenge",
        "version": "1.0",
        "framework": "Flask"
    })


@app.route("/api/redis")
def redis_health():
    try:
        redis_client.set("devops-challenge", "Redis connection successful")
        value = redis_client.get("devops-challenge")
        return jsonify({
            "redis_status": "connected",
            "message": value
        })
    except redis.RedisError as error:
        return jsonify({
            "redis_status": "disconnected",
            "error": str(error)
        }), 503


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
