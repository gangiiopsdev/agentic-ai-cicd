from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Sanitize input to prevent injection attacks
    sanitized_host = shlex.quote(host)
    command = ['ping', sanitized_host]
    subprocess.call(command)
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}