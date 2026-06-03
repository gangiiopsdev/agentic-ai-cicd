from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host):
    # Simple IP address validation, expand as needed
    allowed_ips = ['127.0.0.1', 'localhost']
    if host not in allowed_ips:
        raise ValueError('Invalid host')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
    return {
        'status': 'completed',
        'stdout': result.stdout,
        'stderr': result.stderr
    }