from fastapi import FastAPI
import subprocess
def safe_ping(host):
    # Ensure host input is sanitized or validated
    if not host.isalnum():
        raise ValueError('Invalid input for ping command')
    subprocess.call(["ping", host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}