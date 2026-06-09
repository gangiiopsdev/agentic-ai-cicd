from fastapi import FastAPI
import subprocess
import re

def safe_ping(host: str):
    # Validate and sanitize the input host
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    try:
        full_command = ['ping', host]
        subprocess.run(full_command, check=True)
    except subprocess.CalledProcessError as e:
        print(f'Ping failed with error code {e.returncode}')

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}