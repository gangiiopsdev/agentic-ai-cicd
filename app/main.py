from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) and not re.match(r'^\d+\.\d+\.\d+\.\d+$', host):
        raise ValueError('Invalid hostname')
    # Secure implementation using subprocess.run with shell=False and check=True
    subprocess.run(['ping', '-c 4', host], shell=False, check=True)

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_safe(host: str):
    ping(host)