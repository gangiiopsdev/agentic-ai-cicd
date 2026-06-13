from fastapi import FastAPI
import subprocess
import shlex
global safe_ping, app

app = FastAPI()

def safe_ping(host: str):
    host_parts = shlex.split(host)
    if len(host_parts) == 1 and host.isalnum():
        result = subprocess.run(['ping', host], capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid input')

@app.get('/ping')
def ping(host: str):
    return {'status': safe_ping(host)}