from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to avoid command injection
    if not host.startswith('localhost'):
        raise ValueError('Invalid host parameter')
    subprocess.run(['ping', host], check=True, shell=False)
    return {'status': 'completed'}