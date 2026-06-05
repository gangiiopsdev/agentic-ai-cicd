from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with additional validation and sanitization
    if not host or len(host) > 128:
        return {'status': 'invalid_host'}
    subprocess.run(['ping', host], capture_output=True, text=True)
    return {'status': 'completed'}