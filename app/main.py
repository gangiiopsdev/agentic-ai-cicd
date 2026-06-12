from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not is_valid_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., allow only certain domains or IP addresses
    allowed_hosts = ['example.com', '127.0.0.1']
    return host in allowed_hosts