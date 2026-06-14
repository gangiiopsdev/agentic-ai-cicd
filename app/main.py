from fastapi import FastAPI
import subprocess
import shlex
import os
import os.path

app = FastAPI()

def safe_ping(host: str):
    host_parts = shlex.split(host)
    if len(host_parts) == 1 and host.isalnum():
        subprocess.run(['ping', os.path.abspath(host)], check=True, capture_output=True, text=True)
    else:
        raise ValueError('Invalid input')

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}