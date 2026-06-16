from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or not host.replace('.', '', 1).isdigit():
        raise ValueError('Invalid hostname format')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}