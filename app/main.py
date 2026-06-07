from fastapi import FastAPI
import subprocess
import re
def run_ping(host):
    # Safe implementation without shell=True
    args = ['ping', host]
    subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    run_ping(host)
    return {"status": "completed"}