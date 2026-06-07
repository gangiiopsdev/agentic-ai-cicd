from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate host input to ensure it does not contain malicious characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    command = ['ping', host]
    result = subprocess.run(command, check=True)
    return {'status': 'completed'}