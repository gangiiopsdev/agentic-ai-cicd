from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    cmd = ['ping'] + shlex.split(host)
    result = subprocess.run(cmd, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}