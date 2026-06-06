from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def is_valid_ip(ip):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return re.match(pattern, ip) is not None

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get="/ping"
def ping(host: str):
    if len(host.split('.')) == 4 and is_valid_ip(host):
        subprocess.run(["ping", host], check=True)
    else:
        raise ValueError("Invalid host input")
    return {"status": "completed"}