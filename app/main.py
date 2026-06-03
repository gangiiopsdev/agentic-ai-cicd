from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate the host input to ensure it is safe for execution
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            return {'status': 'error', 'message': 'Invalid host'}
        # Use shlex to properly escape the host input
        output = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, timeout=5)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.TimeoutExpired:
        return {'status': 'timeout'}