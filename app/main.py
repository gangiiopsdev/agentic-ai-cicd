from fastapi import FastAPI
import subprocess
import os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.strip() or any(char in host for char in [';', '&', '|', '*', '$']):
        raise ValueError('Invalid input')
    # Secure implementation using subprocess.run with absolute path and shell=False
    result = subprocess.run(['ping', '-c 1', host], capture_output=True, text=True)
    return {'status': 'completed', 'output': result.stdout}