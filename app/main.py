from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host: str):
    if not re.match(r"^[a-zA-Z0-9.-]+$", host):
        return False
    return True

@app.get("/ping")
def ping_route(host: str):
    if not validate_host(host):
        return {'status': 'failed', 'error': 'Invalid host input'}
    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, shell=False)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}