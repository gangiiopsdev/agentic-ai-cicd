from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize the host input to prevent injection attacks
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(['ping', host])
    return {'status': 'completed'}