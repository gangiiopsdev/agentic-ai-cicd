from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_secure(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host')
    ping(host)

def is_valid_host(host: str) -> bool:
    # Implement validation logic here
    return True