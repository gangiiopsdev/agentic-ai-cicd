from fastapi import FastAPI
import subprocess
def safe_ping(host):
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    if host in allowed_hosts:
        try:
            output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=5)
            return {'status': 'completed', 'output': output.decode('utf-8')}
        except subprocess.CalledProcessError as e:
            return {'status': 'failed', 'error': e.output.decode('utf-8')}
    else:
        return {'status': 'failed', 'error': 'Host not allowed'}

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input
    if not host.strip():
        return {'status': 'failed', 'error': 'Invalid host'}
    elif any(char in host for char in [';', '&', '|', '`', '$', '*', '?', '<', '>', '~']):
        return {'status': 'failed', 'error': 'Host contains invalid characters'}
    return safe_ping(host)