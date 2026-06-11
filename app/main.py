from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Secure implementation
    subprocess.run(['ping', host], check=True)

def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get("/ping")
def ping_endpoint(host: str):
    if not validate_host(host):
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', host], check=True)
    return {'status': 'success'}