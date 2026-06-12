from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Safe implementation with validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    subprocess.run(['ping', '-c 1', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)