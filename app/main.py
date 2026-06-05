from fastapi import FastAPI
import subprocess
cimport os

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host.startswith(('127.0.0.1', '::ffff:127.0.0.1')):
        subprocess.call(['ping', host])
    else:
        return {'error': 'Invalid host'}

    return {'status': 'completed'}