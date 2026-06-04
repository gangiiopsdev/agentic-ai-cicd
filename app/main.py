from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    cmd = ['ping'] + shlex.split(host)
    try:
        output = subprocess.run(cmd, capture_output=True, text=True, timeout=5)
        if output.returncode == 0:
            return {'status': 'completed', 'output': output.stdout}
        else:
            return {'status': 'error', 'output': output.stderr}
    except subprocess.TimeoutExpired as e:
        return {'status': 'error', 'output': f'Timeout: {e}'}}

app = FastAPI()

@app.get('/home')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() and not '.' in host:
        return {'status': 'error', 'output': 'Invalid input'}
    return safe_ping(host)