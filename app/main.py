from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.isalnum()

@app.get('/ping/{host}')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

# Secure fix: Use a whitelist for allowed hosts
ALLOWED_HOSTS = {'example.com', 'localhost'}

@app.get('/ping/{host}')
def ping(host: str):
    if not validate_host(host) or host not in ALLOWED_HOSTS:
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}