from fastapi import FastAPI
import subprocess
from typing import Union

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {'error': 'Invalid host'}

    # Secure implementation using subprocess.run with shell=False and check=True
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'error': str(e)}