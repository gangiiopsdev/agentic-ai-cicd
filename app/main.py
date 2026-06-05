from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    # Add your sanitization logic here to prevent command injection
    allowed_hosts = ['example.com', 'test.com']
    if host in allowed_hosts:
        return host
    else:
        raise ValueError('Host not allowed')

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}