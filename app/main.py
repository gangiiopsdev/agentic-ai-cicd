from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.strip():
        raise ValueError('Host parameter is empty or contains only whitespace. Please provide a valid hostname.')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}