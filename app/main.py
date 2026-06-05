from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Validate input
    allowed_hosts = ['example.com', 'test.com']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Host is not allowed'}
    
    # Secure implementation using subprocess.run
    result = subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}