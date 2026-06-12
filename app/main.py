from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str) -> dict:
    if not host.isalnum() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid input'}
    cmd = ['ping'] + shlex.split(host)
    try:
        output = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid input'}
    cmd = ['ping'] + shlex.split(host)
    try:
        output = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}