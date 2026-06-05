from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Safe implementation with input validation
    if not host.isalnum() or len(host) > 100:
        return {'error': 'Invalid host'}, 400
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}