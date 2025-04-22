import redis

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def query_short_url(short_code: str) -> str:
    long_url = r.get(f"url:{short_code}")
    if long_url:
        r.incr(f"counter:{short_code}")
        return f"Long URL: {long_url}"
    else:
        return f"Short code '{short_code}' not found."
