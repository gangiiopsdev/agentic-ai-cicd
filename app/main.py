from fastapi import FastAPI
import subprocess
import shlex
def run_ping(host: str):
    # Validate input
    if not host.strip() or len(host) > 256:
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        output = subprocess.check_output(['ping', '-c', '4', host], universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping_safe(host: str):
    # Validate input
    if not host.strip() or len(host) > 256:
        return {'status': 'failed', 'error': 'Invalid host name'}
    return run_ping(host)