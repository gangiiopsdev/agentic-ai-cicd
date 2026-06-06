from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host.startswith('192.168.') or host.startswith('localhost'):  # Example whitelist for localhost and local network IPs
        subprocess.call(['ping', host])
    else:
        raise ValueError('Invalid host specified')
    return {'status': 'completed'}