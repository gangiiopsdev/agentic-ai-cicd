from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if host and all(c.isalnum() or c in ('.', '-', '_') for c in host):
        args = ['ping', host]
        subprocess.run(args, check=True)
    else:
        return {'error': 'Invalid hostname'}
    return {'status': 'completed'}