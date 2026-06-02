from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):  # Allow underscores for potential domain names
        raise ValueError('Invalid host name')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}