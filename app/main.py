from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host name'}
    try:
        result = subprocess.run(['ping', f'-c 1 {shlex.quote(host)}'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host name'}
    try:
        result = subprocess.run(['ping', f'-c 1 {shlex.quote(host)}'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}