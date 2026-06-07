from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation with input validation
    allowed_hosts = ['example.com', 'test.example.com']
    if host not in allowed_hosts:
        return {'status': 'error', 'message': 'Invalid host'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}