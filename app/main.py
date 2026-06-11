from fastapi import FastAPI
import re
import subprocess
import shlex

global_host_pattern = re.compile(r'^[a-zA-Z0-9.-]+$')
app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not global_host_pattern.match(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}

def is_valid_host(host: str) -> bool:
    return all(c.isalnum() or c in ['.', '-'] for c in host)