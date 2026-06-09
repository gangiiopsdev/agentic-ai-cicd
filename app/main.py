from fastapi import FastAPI
import subprocess
import re

global BLACKLIST
BLACKLIST = ['; ', '|', '&', '&&', '||']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if any(keyword in host for keyword in BLACKLIST):
        return {'status': 'failed', 'error': 'Invalid characters in host'}
    try:
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}