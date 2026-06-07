from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced validation with regex to allow only valid hostnames/IP addresses
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'invalid input'}
    command = ['ping'] + shlex.split(host)
    subprocess.run(command, check=True)
    return {'status': 'completed'}