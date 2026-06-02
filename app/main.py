from fastapi import FastAPI
import subprocess
cimport subprocess

app = FastAPI()

def safe_ping(host):
    allowed_hosts = ['192.168.1.1', '10.0.0.1']  # Example list of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    sanitized_host = subprocess.quote(host)
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)