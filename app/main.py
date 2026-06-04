from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with validation and escaping
    if 'localhost' in host or '127.0.0.1' in host:
        subprocess.call(['ping', host])
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid host')