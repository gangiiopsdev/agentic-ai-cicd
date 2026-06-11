from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Sanitize the host input using shlex.quote
    safe_host = shlex.quote(host)
    subprocess.call(['ping', '-c 4', safe_host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with sanitized input
    safe_ping(host)
    return {"status": "completed"}