from fastapi import FastAPI
import subprocess
def validate_host(host):
    # Simple validation, in a real scenario use a whitelist of allowed hosts
    return host.replace('.', '_').isalnum()

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        result = subprocess.run(['ping', '-c', '1', f'/usr/bin/ping'], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}