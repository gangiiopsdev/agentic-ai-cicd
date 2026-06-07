from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    host = host.strip()
    if not re.match(r'^[a-zA-Z0-9]+$', host):  # Allow only alphanumeric characters
        return {'status': 'invalid'}
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}