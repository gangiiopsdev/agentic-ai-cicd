from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple validation to ensure the host is a valid IP or domain
    if not (host.startswith('192.') or host.startswith('10. ') or host.startswith('172.') or '.' in host):
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    try:
        validate_host(host)
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output': e.stderr}