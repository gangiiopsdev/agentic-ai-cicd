from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        subprocess.run(['ping', host], check=True, timeout=5)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}