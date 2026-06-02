from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation
    sanitized_host = host.strip()
    if not all(c.isalnum() or c in '._-' for c in sanitized_host):
        return {'status': 'error', 'message': 'Invalid host name'}
    subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}