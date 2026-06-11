from fastapi import FastAPI
import subprocess
import shlex
def sanitize_host(host):
    if not host or len(host) > 255:
        raise ValueError('Invalid host parameter')
    return host.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'error': e.stderr}