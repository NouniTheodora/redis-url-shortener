import redis

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def get_user_stats(username: str) -> str:
    urls = r.lrange(f"user:{username}:urls", 0, -1)
    output = [f"User '{username}' has inserted {len(urls)} URLs:"]

    for short_code in urls:
        long_url = r.get(f"url:{short_code}")
        output.append(f"• {short_code} → {long_url}")

    return "\n".join(output)

def get_average_views() -> str:
    total_views = 0
    count = 0

    for key in r.scan_iter("counter:*"):
        value = r.get(key)
        if value is not None:
            total_views += int(value)
            count += 1

    if count == 0:
        return "No short URLs have been queried yet."

    average = total_views / count
    return f"Average views per short URL: {average:.2f}"
