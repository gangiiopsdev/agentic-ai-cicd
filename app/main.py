from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

def ping(host: str):
    # Secure implementation with validation
    if host not in ['127.0.0.1', 'localhost']:
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)