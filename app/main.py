from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Validate and sanitize input
    if not host.strip().isalnum():
        raise ValueError('Invalid host name')

    cimport = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': cimport.stdout.strip()}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)