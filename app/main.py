from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input
    if not host or len(host) > 255 or any(c not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_' for c in host):
        return {'error': 'Invalid host'}, 400
    subprocess.run(['ping', '-c', str(1), host], check=True, text=True)
    return {'status': 'completed'}