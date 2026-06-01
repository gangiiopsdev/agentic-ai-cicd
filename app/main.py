from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.run(['ping', host], check=True, capture_output=True)
    return {'status': 'completed'}