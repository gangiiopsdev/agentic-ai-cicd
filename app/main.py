from fastapi import FastAPI
import subprocess
def validate_host(host):
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

def ping(host: str):
    validate_host(host)
    # Use a whitelist of allowed hosts for the ping command
    allowed_hosts = ['localhost', '127.0.0.1']
    if host not in allowed_hosts:
        return {'status': 'not_allowed'}
    try:
        subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get('/ping')
def ping_route(host: str):
    return ping(host)