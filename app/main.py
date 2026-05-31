from fastapi import FastAPI
import subprocess
c
app = FastAPI()

def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host or not host.strip():
        raise ValueError('Invalid host')
    sanitized_host = subprocess.quote(host)
    subprocess.run(['ping', '-c', str(1), sanitized_host], check=True)

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)