from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate and sanitize host input
    if not host or len(host) > 255:
        return {'status': 'error', 'error': 'Invalid host'}
    command = ['ping', '-c', '1'] + shlex.split(host)
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)