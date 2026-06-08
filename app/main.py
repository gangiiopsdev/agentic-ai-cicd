from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation and sanitization
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host name")
    command = ["ping", host]
    subprocess.run(command, check=True)
    return {"status": "completed"}