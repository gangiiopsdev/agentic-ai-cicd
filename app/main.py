from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters and does not resemble a command
    if re.match(r'^[a-zA-Z0-9.-]+$', host) is None or any(keyword in host for keyword in [';', '&', '|', '(', ')']):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}