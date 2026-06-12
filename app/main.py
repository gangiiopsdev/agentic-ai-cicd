from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and command sanitization
    if not host.isalnum() or len(host) > 20:
        return {'error': 'Invalid host'}, 400
    subprocess.call(['ping', '-c', '1', host], shell=False)
    return {'status': 'completed'}