from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    if not all(c.isalnum() for c in host):
        raise ValueError('Invalid hostname')
    return host

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_host = safe_ping(host)
    subprocess.run(['ping', safe_host], check=True, capture_output=True)
    return {'status': 'completed'}