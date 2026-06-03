from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid input'}
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}