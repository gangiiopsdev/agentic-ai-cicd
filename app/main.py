from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using subprocess.run with validation
    if not host.isalnum():
        raise ValueError('Invalid input')
    subprocess.run(['ping', f'127.0.0.1 -c 4 {host}'], check=True, timeout=5)

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}