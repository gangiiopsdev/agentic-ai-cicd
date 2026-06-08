from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Input validation to allow only alphanumeric characters and dots
    if not re.match(r'^[a-zA-Z0-9.]+$', host):
        return {'status': 'failed', 'error': 'Invalid input'}

    try:
        subprocess.call(["ping", host], shell=False)
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}