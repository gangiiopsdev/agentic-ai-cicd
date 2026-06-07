from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')


def safe_ping(host: str):
    try:
        validate_host(host)
        subprocess.run(['ping', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    try:
        return safe_ping(host)
    except ValueError as e:
        return {'status': 'failed', 'error': str(e)}