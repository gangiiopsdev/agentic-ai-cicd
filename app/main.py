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
    if not host.isalnum() and '-' not in host:
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', shlex.quote(host)], check=True)
    return {'status': 'completed'}