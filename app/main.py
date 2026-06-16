from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):  # Simplified regex for alphanumeric and common special characters
        raise ValueError("Invalid host parameter")

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get(")
def ping(host: str):
    validate_host(host)
    command = ["ping", shlex.quote(host)]
    subprocess.run(command, check=True)  # Use run instead of call for better error handling
    return {"status": "completed"}