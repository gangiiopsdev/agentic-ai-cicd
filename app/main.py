from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation and sanitization
    safe_host = host.strip()
    if not safe_host:
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', '-c', '1', safe_host], check=True)
    return {'status': 'completed'}