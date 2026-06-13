from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

@app.get('/ping/{host}')
def ping(host: str):
    if not all(c.isalnum() or c in ['.', '-'] for c in host):
        return {'status': 'error', 'message': 'Invalid input'}
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}