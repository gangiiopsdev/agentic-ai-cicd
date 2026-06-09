from fastapi import FastAPI
import subprocess

app = FastAPI()

def validate_host(host: str):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    for char in host:
        if char not in allowed_chars:
            return False
    return True

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid hostname'}
    # Secure implementation using subprocess.run
    result = subprocess.run(['ping', host], capture_output=True, text=True, check=False)
    if result.returncode != 0:
        return {'status': 'error', 'message': 'Ping failed', 'output': result.stderr}
    return {'status': 'completed', 'output': result.stdout}