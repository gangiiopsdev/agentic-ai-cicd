from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    if not host.isalnum() or '.' in host:
        return False, {'status': 'failed', 'error': 'Invalid host name'}
    return True, None

@app.get('/ping')
def ping(host: str):
    valid, error = validate_host(host)
    if not valid:
        return error
    try:
        # Use a safe way to build the command to avoid shell injection
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}