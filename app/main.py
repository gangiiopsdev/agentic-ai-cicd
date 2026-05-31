from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum() or '-' in host or '.' in host:
        raise ValueError('Invalid input')
    args = ['ping', f'-c 1 {host}']
    subprocess.run(args, check=True)
    return {'status': 'completed'}