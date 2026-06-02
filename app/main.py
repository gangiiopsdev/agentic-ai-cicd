from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

allowed_hosts: List[str] = ['example.com', 'test.com']  # Example list of allowed hosts

def ping(host: str):
    if host in allowed_hosts:
        # Secure implementation with full path and shell=False
        subprocess.run(['ping', '-c', '1', host], check=True)
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping_route(host: str):
    try:
        return ping(host)
    except ValueError as e:
        return {'error': str(e)}, 400