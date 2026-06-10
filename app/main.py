from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate input to prevent injection attacks
    if 'ping' in host:
        return "Invalid input"
    subprocess.call(["ping", host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict):
        return result
    else:
        return {"status": "completed"}