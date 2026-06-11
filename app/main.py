from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str) -> str:
    if not re.match(r'^[a-zA-Z0-9.]+$', host) or '.' not in host:
        raise ValueError("Invalid host input")
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return output.stdout
    except subprocess.CalledProcessError as e:
        return e.stderr

@app.get('/')
def home():
    return {"message": 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return {"status": 'completed', "output": safe_ping(host)}