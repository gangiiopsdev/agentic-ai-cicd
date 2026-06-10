from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the input host
    if not host.strip().isalnum():
        raise ValueError("Invalid host name")
    subprocess.run(['ping', shlex.quote(host)], check=True)
    return {"status": "completed"}