from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation using subprocess.run with shell=False and input validation
    if not host:
        raise ValueError('Host parameter is required')
    subprocess.run(['ping', '-c', '1', host], check=True, capture_output=True, text=True)
    return {'status': 'completed'}