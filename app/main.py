from fastapi import FastAPI
import subprocess
import shlex
def secure_ping(host: str):
    # Validate and sanitize the host input
    if not (host.startswith('localhost') or host.startswith('127.0.0.1')):
        return {'status': 'invalid', 'message': 'Invalid host'}
    try:
        command = ['ping'] + shlex.split(host)
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return secure_ping(host)