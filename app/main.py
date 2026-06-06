from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or len(host) > 63:
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {'status': 'completed'}