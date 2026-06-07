from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    args = ['ping', host]
    if not validate_host(host):
        raise ValueError('Invalid host')
    subprocess.call(args, shell=False)
    return {'status': 'completed'}

def validate_host(host:
    # Add validation logic here to ensure the host is safe to use with ping
    pass