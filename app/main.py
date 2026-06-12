from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def safe_ping(host):
    try:
        # Using subprocess.run with shell=False for better security
        subprocess.run(['ping', '-c', '1', host], check=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate input to ensure it does not contain malicious characters
    if not host.replace('.', '').isdigit():
        return {'status': 'failed', 'error': 'Invalid input'}
    return safe_ping(host)