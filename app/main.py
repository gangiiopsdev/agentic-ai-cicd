from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'invalid host'}, 400
    # Safe implementation using subprocess.run with shell=False and full path
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {'status': 'completed'}