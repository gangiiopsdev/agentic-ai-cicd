from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input to ensure it is safe
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    # Secure implementation using subprocess.run with shell=False
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Add validation logic here, e.g., regex to allow only valid IP addresses or domain names
    import re
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None