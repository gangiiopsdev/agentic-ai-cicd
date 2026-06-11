from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host or not isinstance(host, str) or len(host) > 255:
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        subprocess.run([os.path.join(os.sep, 'bin', 'ping'), host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}