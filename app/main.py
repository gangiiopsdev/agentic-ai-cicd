from fastapi import FastAPI
import subprocess
def ping(host: str):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, timeout=10)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

app = FastAPI()

def validate_host(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Add allowed hosts here
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping_route(host: str = Query(..., description='Host to ping')):
    validate_host(host)
    return ping(host)