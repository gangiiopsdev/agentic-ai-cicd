from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the input to prevent command injection
    if host.strip() != host or host.startswith('-'):  # Basic validation example
        raise ValueError('Invalid host name')
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}