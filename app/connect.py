import redis

r = redis.Redis(host="redis", port=6379, decode_responses=True)

welcome = r.get("welcome_message")
print("🔗 Welcome message from Redis:", welcome)
