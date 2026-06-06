from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid host name'}
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}