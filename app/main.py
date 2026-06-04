from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Safe implementation with validation
    if not host or len(host) > 255:
        return {'error': 'Invalid host input'}
    subprocess.call(['ping', host], shell=False)
    return {'status': 'completed'}