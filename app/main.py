from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it is a valid hostname or IP address
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'invalid host'}, 400
    # Safe implementation using subprocess.run with shell=False and full path
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {'status': 'completed'}