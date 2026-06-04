from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not is_valid_host(host):
        return {'error': 'Invalid host'}
    
    # Fixed implementation
    subprocess.call(['ping', host])
    
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Add your validation logic here, e.g., check if the host is in a whitelist
    allowed_hosts = ['example.com']
    return host in allowed_hosts