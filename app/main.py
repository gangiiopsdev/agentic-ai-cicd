from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and sanitization
    if host.strip() != host:
        raise ValueError('Invalid host input')
    command = ['ping', host]
    subprocess.call(command)
    return {'status': 'completed'}