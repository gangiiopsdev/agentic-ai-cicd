from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        # Validate input to prevent command injection
        if not host.isalnum():
            return {'status': 'failed', 'error': 'Invalid input'}
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}