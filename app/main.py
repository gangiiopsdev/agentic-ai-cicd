from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to avoid injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid host'}, 400
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}