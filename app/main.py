from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ('.', '-') for c in host):
        raise ValueError('Invalid host name')
    subprocess.call(["ping", host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except ValueError as e:
        return {"error": str(e), "status": "failed"}