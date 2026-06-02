from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent injection attacks
    if not host.isalnum() or len(host) > 100:
        return {'error': 'Invalid host'}, 400
    # Secure implementation
    subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed'}