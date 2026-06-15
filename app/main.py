from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not os.path.basename(host) == host or '@' in host:
        raise ValueError("Invalid host")
    command = ["ping", shlex.quote(host)]
    subprocess.run(command, check=True)
    return {"status": "completed"}