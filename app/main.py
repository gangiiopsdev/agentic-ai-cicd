from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host: str):
    # Regex to allow only letters and numbers
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        raise ValueError("Invalid hostname")
    command = ['ping', '-c', '1'] + shlex.split(host)
    subprocess.run(command, check=True)

@app.get="/home")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}