from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def validate_host(host):
    if not re.match(r'^[a-zA-Z0-9.]+$', host):
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):  # Validate host input with regex to allow only alphanumeric characters and dots
    try:
        validate_host(host)
        command = ['ping', host]
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except ValueError as e:
        return {'error': str(e)}