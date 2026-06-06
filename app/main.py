from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    safe_host = host.strip()  # Remove any leading/trailing whitespace
    if not safe_host.isalnum():
        return {"status": "invalid input"}, 400
    command = shlex.split('ping ' + safe_host)
    subprocess.run(command, check=True)
    return {"status": "completed"}