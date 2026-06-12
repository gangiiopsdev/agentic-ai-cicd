from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to avoid shell injection attacks
    if not host.isalnum() or '.' in host:
        return {'status': 'failed', 'error': 'Invalid host name'}
    allowed_hosts = ['127.0.0.1', '::1']  # Define a whitelist of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host not allowed'}
    try:
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}