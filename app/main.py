from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

allowed_hosts = ['127.0.0.1', '::1']  # Define allowed hosts

def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in allowed_hosts:
        raise ValueError('Invalid host')

    try:
        result = subprocess.run(['ping', '-c', '1', host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return {'host': host, 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'host': host, 'error': str(e)}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)