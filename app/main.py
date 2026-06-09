from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        raise ValueError('Invalid input for ping request')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}