from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']  # Define a list of allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    try:
        output = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}