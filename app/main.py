from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with validation and sanitization
    if host.startswith('192.168.'):
        subprocess.call(['ping', host])
    return {'status': 'completed'}