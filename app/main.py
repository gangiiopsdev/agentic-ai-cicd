from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return {'error': 'Invalid host name'}
    subprocess.run(['ping', host], shell=False)
    return {'status': 'completed'}