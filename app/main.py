from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'error', 'message': 'Invalid input'}
    try:
        args = shlex.split(f'ping -c 4 {host}')  # Use shlex for safe splitting of command arguments
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e)}