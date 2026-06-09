from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent injection attacks
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid hostname provided')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}