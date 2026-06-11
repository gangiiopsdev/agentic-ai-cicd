from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9-.]{1,}$', host):
        raise ValueError('Invalid host name')
    subprocess.run(["/bin/ping", host], check=True, shell=False)
    return {'status': 'completed'}