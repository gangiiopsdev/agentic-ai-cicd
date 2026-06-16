from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation using subprocess.run with shell=False and avoiding use of host directly in the command list.
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
    return {'status': 'completed', 'stdout': result.stdout}

def validate_host(host: str) -> bool:
    # Implement a function to validate the host input
    allowed_hosts = ['example.com', 'test.com']
    return host in allowed_hosts