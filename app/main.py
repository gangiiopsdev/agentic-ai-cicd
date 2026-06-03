from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate the input to allow only alphanumeric characters and a limited set of safe symbols
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        return {"error": "Invalid hostname"}
    args = shlex.split(f'ping -c 1 {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}