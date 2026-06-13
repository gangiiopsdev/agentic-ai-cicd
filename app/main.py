from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with input validation and sanitization
    if not host.isalnum() or len(host) > 255:
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}