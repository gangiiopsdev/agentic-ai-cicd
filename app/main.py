from fastapi import FastAPI
import subprocess

global app
app = FastAPI()

def safe_ping(host):
    # Use a safer way to handle ping without shell=True
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get('/ping')
def ping(host: str):
    # Validate host to avoid injection attacks
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return safe_ping(host)

def validate_host(host):
    allowed_hosts = ['example.com']  # Replace with actual allowed hosts
    return host in allowed_hosts