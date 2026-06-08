from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to ensure it only contains allowed characters
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}