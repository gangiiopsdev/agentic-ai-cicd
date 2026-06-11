from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and sanitization
    if not host.isalnum():
        return {'error': 'Invalid input'}
    sanitized_host = ''.join(filter(str.isalnum, host))
    subprocess.call(['ping', sanitized_host])
    return {'status': 'completed'}