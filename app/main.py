from fastapi import FastAPI
import subprocess

app = FastAPI()

def safe_ping(host: str):
    try:
        # Use subprocess.run for safer execution
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

def validate_host(host: str):
    # Add validation logic to ensure the host is safe to ping
    allowed_hosts = ['127.0.0.1', '::1']  # Example list of allowed hosts
    if host not in allowed_hosts:
        return {'status': 'failed', 'error': 'Host not allowed'}
    return safe_ping(host)

@app.get('/ping')
def ping(host: str):
    return validate_host(host)