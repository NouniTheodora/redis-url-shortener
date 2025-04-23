# redis-url-shortener
A simple URL shortener implemented in Python using Redis. Supports insertion, query, and usage statistics tracking.

The application supports:
- Insertion of long URLs (with automatic short code generation)
- Querying short URLs to retrieve the original
- Tracking usage statistics (per-user insertions & average views)

## Setup

Make sure you have [Docker](https://www.docker.com/products/docker-desktop) installed.

```bash
docker compose up --build -d
```
This will start:

- Redis database

- RedisInsight GUI (http://localhost:8001)

- Python application container (for running the app)

## Run the app
Start the CLI app:

```bash
docker exec -it uom-redis-url-shortener-app bash
python app/main.py
```
You’ll be asked for a username, then you can perform actions via the menu.

![alt text](redis-url-shortener-example.png)

![alt text](redis-url-shortener-example-2.png)

## Demo Recording (Terminal Script)

A demonstration of the application's functionality has been recorded using the script and scriptreplay tools inside the Python Docker container.

Two files are included in the demo/ folder:
- myscript → captures the terminal output
- mytimelog → captures timing information

These allow the full session to be replayed exactly as it occurred.

## How to replay the demo
```bash
scriptreplay -t demo/mytimelog demo/myscript
```
The recording was made inside the container uom-redis-url-shortener-app using:
```bash
apt update && apt install -y util-linux
script -T mytimelog myscript
```
You can view or repeat the session exactly as it was executed.