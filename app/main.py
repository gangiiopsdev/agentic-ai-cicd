from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host):
    if not re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\\\.[0-9]{1,3}\\\.[0-9]{1,3}$', host):
        raise ValueError('Invalid IP address')
    subprocess.run(['ping', '-c', '1', host], check=True)

@app.get('/ping')
def ping(host: str):
    safe_ping(host)
    return {'status': 'completed'}