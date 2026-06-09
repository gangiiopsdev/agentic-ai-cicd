from fastapi import FastAPI
import subprocess

app = FastAPI()

def is_safe_host(host):
    # Add your own logic to validate the host input
    return '127.0.0.1' in host or 'localhost' in host

@app.get('/ping')
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    # Secure implementation using subprocess.run with shell=False
    result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}