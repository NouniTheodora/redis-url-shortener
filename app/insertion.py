import redis
import random
import string

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def insert_url(long_url, username):
    existing = r.get(f"long:{long_url}")
    if existing:
        return f"URL already exists! Short code: {existing}"

    short_code = generate_short_code()
    while r.exists(f"url:{short_code}"):
        short_code = generate_short_code()

    r.set(f"url:{short_code}", long_url)
    r.set(f"long:{long_url}", short_code)
    r.rpush(f"user:{username}:urls", short_code)

    return f"New short URL created: {short_code}"

if __name__ == "__main__":
    long_url = input("Enter long URL: ")
    username = input("Enter your username: ")
    print(insert_url(long_url, username))