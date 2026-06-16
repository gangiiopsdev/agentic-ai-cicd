from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Input validation and sanitization
    allowed_hosts = ['127.0.0.1', '::1']
    if host not in allowed_hosts or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid input'}
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}