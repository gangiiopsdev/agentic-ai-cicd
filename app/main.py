from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    subprocess.run(['ping', host], check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host input')
    ping(host)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Add validation logic here
    return host.strip() and '.' in host