from fastapi import FastAPI
import subprocess
from pydantic import validator

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        # Validate input to ensure it does not contain malicious content
        if any(char in host for char in [';', '&', '|', '`']):
            raise ValueError('Invalid characters in host parameter')
        result = subprocess.run(['ping', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}