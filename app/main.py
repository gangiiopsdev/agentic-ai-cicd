from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation
    if not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    args = ['ping', host]
    try:
        subprocess.run(args, check=True)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}