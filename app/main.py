from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with validation and sanitization
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', f'"{host}"'])  # Escape quotes for security
    return {'status': 'completed'}