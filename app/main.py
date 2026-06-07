from fastapi import FastAPI
import subprocess

app = FastAPI()

def secure_ping(host: str):
    # Secure implementation
    args = ['ping', host]
    subprocess.call(args)
    return {'status': 'completed'}

@app.get('/ping')
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid hostname')
    secure_ping(host)
    return {'status': 'completed'}

def is_valid_host(host: str) -> bool:
    # Implement validation logic here, e.g., regex check for allowed characters
    return all(c.isalnum() or c in ['.', '-'] for c in host)