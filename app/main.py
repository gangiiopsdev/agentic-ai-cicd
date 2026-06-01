from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation with input validation
    if host.isalnum() and len(host) <= 64:
        subprocess.call(['ping', '-c', '1', host])
        return {'status': 'completed'}
    else:
        return {'error': 'Invalid input'}, 400