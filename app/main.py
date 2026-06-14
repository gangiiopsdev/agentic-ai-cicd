from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Safe implementation with validation and sanitization
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    safe_host = re.sub(r'[^a-zA-Z0-9.-]', '', host)
    subprocess.run(['ping', '-c 4', safe_host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)