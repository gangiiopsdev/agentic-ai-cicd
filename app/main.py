from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize user input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host])
    return {'status': 'completed'}