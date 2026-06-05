from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Enhanced validation with regex to allow only valid hostnames/IP addresses
    import re
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {'status': 'invalid input'}
    command = ['ping', host]
    subprocess.call(command, shell=False)
    return {'status': 'completed'}