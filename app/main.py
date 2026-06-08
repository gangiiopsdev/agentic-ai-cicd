from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host.isalnum():
        raise ValueError("Invalid host name")
    command = ['ping'] + shlex.split(host)
    subprocess.run(command, check=True, capture_output=True)
    return {"status": "completed"}