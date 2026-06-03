from fastapi import FastAPI
import re
import subprocess

app = FastAPI()

def validate_host(host: str) -> bool:
    return re.match(r'^[a-zA-Z0-9.-]+$', host) is not None

@app.get('/ping')
def ping(host: str):
    if not validate_host(host):
        return {'status': 'invalid_host'}
    subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
    return {'status': 'completed'}