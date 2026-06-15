from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9]{1,255}$', host):
        raise ValueError('Invalid host name')
    subprocess.run(['ping', host], check=True)
    return {'status': 'completed'}