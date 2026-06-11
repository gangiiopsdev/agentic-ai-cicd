from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    args = ['ping', host]
    result = subprocess.run(args, check=True, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {"status": "completed", "output": result.stdout.decode(), "error": result.stderr.decode()}