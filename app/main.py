from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host):
    # Secure implementation using subprocess.run with shell=False and validate_host function
    if not validate_host(host):
        raise ValueError('Invalid host name')
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)

def validate_host(host):
    # Add validation logic here to ensure the host is safe to ping
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts