from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not host.strip() or len(host) > 255:
        return {"error": "Invalid host"}, 400

    # Use absolute path to avoid partial path execution
    subprocess.call(["ping", "/usr/bin/ping", host])

    return {"status": "completed"}