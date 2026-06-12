from fastapi import FastAPI
import subprocess
import shlex
import re

def is_valid_host(host: str) -> bool:
    # Regex pattern to allow only valid hostname characters
    regex = r'^[a-zA-Z0-9.-_]+$'
    return re.match(regex, host)

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}

    # Use subprocess.run with check=True to handle errors gracefully
    try:
        result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}