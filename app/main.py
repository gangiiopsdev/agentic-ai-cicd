from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Fixed implementation with proper sanitization
    if not host.isalnum():
        raise ValueError('Invalid input')
    subprocess.run(['ping', host], check=True, text=True)
    return {'status': 'completed'}