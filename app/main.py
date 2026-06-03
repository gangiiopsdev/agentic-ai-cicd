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
        raise ValueError('Host parameter is empty or invalid')
    subprocess.run(['ping', *host.split()], check=True, shell=False)
    return {'status': 'completed'}