from fastapi import FastAPI
import subprocess

def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']  # Define allowed hosts
    if host not in allowed_hosts:
        raise ValueError('Host is not allowed')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    try:
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True, shell=False)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

# Add input validation for host parameter
def validate_host(host):
    allowed_hosts = ['example.com', 'test.example.com']  # Define allowed hosts
    if not any(host.endswith(allowed) for allowed in allowed_hosts):
        raise ValueError('Host is not allowed')