from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with input sanitization and validation
    if host.strip() and all(c.isalnum() for c in host) and len(host) <= 255:
        subprocess.call(['ping', host], shell=False)
    else:
        return {'status': 'error', 'message': 'Invalid input'}
    return {'status': 'completed'}