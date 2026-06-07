from fastapi import FastAPI
import subprocess
import shlex
def validate_host(host: str) -> bool:
    return all(c.isalnum() or c in ('.', '-') for c in host)
app = FastAPI()
@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host)}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}