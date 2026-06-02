from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with validation and sanitization
    if not host.isalnum():
        return {'status': 'invalid'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}