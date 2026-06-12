from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isdigit() or int(host) > 255:
        raise ValueError('Invalid host input')
    subprocess.run(['ping', '-c', '1', host], check=True)
    return {'status': 'completed'}