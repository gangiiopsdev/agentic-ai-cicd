from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid host name')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}