from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation
    if not validate_host(host):
        return {'error': 'Invalid host'}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}

def validate_host(host: str) -> bool:
    allowed_hosts = ['example.com']  # Define a list of allowed hosts
    return host in allowed_hosts

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_endpoint(host: str):
    return ping(host)