from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host and len(host) < 100:
        subprocess.call(['ping', host])
    else:
        return {'error': 'Invalid input'}

    return {'status': 'completed'}