from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Sanitize input to avoid command injection
    if 'ping' not in host and 'localhost' not in host:
        raise ValueError('Invalid host parameter')
    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}