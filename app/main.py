from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with proper input validation and sanitization
    if not host.isalnum() or len(host) > 255:
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}