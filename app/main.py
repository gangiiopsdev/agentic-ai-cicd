from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the host input
    if not host.isdigit():
        raise ValueError('Invalid host input. Only numeric values are allowed.')
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True, check=True)
    return {'status': 'completed', 'output': result.stdout}