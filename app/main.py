from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not all(c.isalnum() or c in ['-', '.'] for c in host):
        return {'error': 'Invalid host input'}, 400
    command = shlex.split('ping ' + host)
    subprocess.call(command, shell=False)
    return {'status': 'completed'}