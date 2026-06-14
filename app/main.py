from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host and re.match(r'^[a-zA-Z0-9.-_]+$', host):
        args = ['ping', host]
        subprocess.run(args, check=True)
    else:
        return {'error': 'Invalid hostname'}
    return {'status': 'completed'}