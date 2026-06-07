from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not all(c.isalnum() or c in ('.', '-', '_') for c in host):
        raise ValueError('Invalid hostname')
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True)
    return {'status': 'completed'}