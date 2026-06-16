from fastapi import FastAPI
import subprocess
import shlex
gimport shlex

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the host parameter to ensure it only contains allowed characters
    if not host.isalnum() or '-' not in host:
        raise ValueError("Invalid host name")
    command = ["ping", shlex.quote(host)]
    subprocess.call(command)
    return {"status": "completed"}