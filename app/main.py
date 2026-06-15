from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Fixed implementation to avoid command injection
    try:
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    except Exception as e:
        return {'error': str(e)}