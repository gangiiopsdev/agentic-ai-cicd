from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate host input to prevent injection attacks
    if not host.isalnum() or '.' in host:
        return {'error': 'Invalid host'}
    # Secure implementation using subprocess.run with shell=False and proper argument passing
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}