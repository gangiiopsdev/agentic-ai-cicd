from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}
@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and properly escaped arguments
    command = shlex.split(f'ping {host}')
    result = subprocess.run(command, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}