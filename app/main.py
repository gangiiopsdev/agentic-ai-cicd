from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host.startswith('192.168.') or host.startswith('localhost'):  # Example of a simple whitelist
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid host'}, 400