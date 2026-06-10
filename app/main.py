from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation and sanitization
    if not host or ' ' in host or host.isnumeric() or host.startswith('-'):
        return {'error': 'Invalid input'}, 400
    subprocess.call(['ping', '-c', '1', host])
    return {'status': 'completed'}