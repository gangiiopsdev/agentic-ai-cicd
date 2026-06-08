from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the input to ensure it does not contain malicious content
        if not host.isnumeric() or len(host.split('.')) != 4:
            return {'status': 'failed', 'error': 'Invalid host'}
        cmd = shlex.split(f'ping {host}')
        output = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return {'status': 'failed', 'error': str(e)}