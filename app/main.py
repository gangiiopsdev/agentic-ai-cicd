from fastapi import FastAPI
import subprocess
from typing import List

app = FastAPI()

def validate_host(host: str) -> bool:
    # Basic validation, add more checks based on requirements
    allowed_hosts = ['example.com', 'localhost']
    return host in allowed_hosts

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        raise ValueError('Invalid host')

    args = ['ping', host]
    subprocess.call(args)

    return {'status': 'completed'}