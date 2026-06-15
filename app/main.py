from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host):
    if not host.isalnum():
        return False
    # Additional validation can be added here
    return True

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host name'}

    # Use a whitelist of allowed hosts instead of validating the input with regex
    allowed_hosts = ['host1', 'host2']  # Example list
    if host in allowed_hosts:
        subprocess.run(shlex.split(f'ping {host}'), check=True, capture_output=True)
        return {'status': 'completed'}
    else:
        return {'status': 'error', 'message': 'Host not allowed'}