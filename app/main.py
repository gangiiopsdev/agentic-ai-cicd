from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize user input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or 'ping' in host:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        command = ['ping', '-c', '1'] + shlex.split(f'-- {host}')
        output = subprocess.run(command, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}