from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation
    if host.strip() and all(c.isalnum() or c in '.-' for c in host):  # Basic validation of the host parameter
        subprocess.call(['ping', host])
    return {'status': 'completed'}