from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Properly sanitize and validate the input
    if not host.strip() or any(c in host for c in (';', '|', '&', '$', '`')):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed'}