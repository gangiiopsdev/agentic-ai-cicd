from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced validation using regex to allow valid hostnames and IPs
    if host.strip() and re.match(r'^[a-zA-Z0-9.-]+$', host):  # Improved validation example
        subprocess.run(['ping', '-c', '1', host], check=True)
        return {'status': 'completed'}
    else:
        raise ValueError('Invalid hostname')