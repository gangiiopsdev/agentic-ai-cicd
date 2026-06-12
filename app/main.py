from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host name")
    try:
        result = subprocess.run(['ping', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=False)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)