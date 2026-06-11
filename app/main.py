from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

allowed_hosts = {'example.com', 'localhost'}

def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host) or host not in allowed_hosts:
        raise ValueError('Invalid host')
    subprocess.run(['ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)