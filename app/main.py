from fastapi import FastAPI
import subprocess
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and input sanitization
    if not validate_host(host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation using subprocess.run with shell=False and input sanitization
    if not validate_host(host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)
    return {"status": "completed"}

def validate_host(host: str) -> bool:
    # Basic validation of host format
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None