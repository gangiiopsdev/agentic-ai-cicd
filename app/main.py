from fastapi import FastAPI
import subprocess
import re

cimport os

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with basic input validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'error': 'Invalid hostname'}
    command = ['ping', host]
    subprocess.run(command, check=True)
    return {'status': 'completed'}