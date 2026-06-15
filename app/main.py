from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input
    if not host or ' ' in host:
        return {'status': 'failed', 'error': 'Invalid host'}

    # Additional validation for safe characters only
    if re.search(r'[^a-zA-Z0-9.-]', host):
        return {'status': 'failed', 'error': 'Unsafe characters in host'}

    try:
        result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}