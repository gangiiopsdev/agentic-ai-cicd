from fastapi import FastAPI
import subprocess
from shlex import quote

def ping(host: str):
    # Secure implementation using subprocess.run()
    try:
        subprocess.run(["ping", quote(host)], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping_host(host: str):
    # Secure implementation using subprocess.run()
    try:
        subprocess.run(["ping", quote(host)], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}