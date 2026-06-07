from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping(host: str):
    # Secure implementation using subprocess.run instead of subprocess.call
    args = ['ping', host]
    result = subprocess.run(args, check=True)
    return {'status': 'completed'}

@app.get('/ping')
def ping_secure(host: str):
    if not all(c.isalnum() or c in '-.' for c in host):
        raise ValueError('Invalid host name')
    return ping(host)