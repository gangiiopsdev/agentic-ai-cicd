from fastapi import FastAPI
import subprocess
c
app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

def ping(host: str):
    # Secure implementation with input validation
    if not host or not host.strip():
        raise ValueError('Invalid host')
    subprocess.run(['ping', '-c', str(1), host], check=True)

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)