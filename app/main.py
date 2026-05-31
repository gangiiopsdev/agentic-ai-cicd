from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    return ping(host)

def validate_host(host: str):
    allowed_hosts = ['example.com', 'localhost']  # Add allowed hosts here
    return all(char.isalnum() or char in ['-.', ':'] for char in host)