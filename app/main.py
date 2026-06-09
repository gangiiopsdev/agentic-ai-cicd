from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Enhanced sanitization to ensure safe input
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid input")
    command = ['ping', shlex.quote(host)]
    subprocess.call(command)
    return {"status": "completed"}