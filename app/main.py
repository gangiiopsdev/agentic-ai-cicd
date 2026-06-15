from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host: str) -> bool:
    return host and ' ' not in host and re.match(r'^[a-zA-Z0-9._-@]+$', host)

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', shlex.quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}