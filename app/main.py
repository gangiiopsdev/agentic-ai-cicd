from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize the input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]{1,255}$', host):
        raise ValueError('Invalid hostname provided')
    # Use subprocess.run with shell=False and check=True
    command = ['ping', host]
    subprocess.run(command, shell=False, check=True)
    return {'status': 'completed'}