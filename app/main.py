from fastapi import FastAPI
import re
import subprocess

def ping(host: str):
    # Safer implementation with proper sanitization
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host])

app = FastAPI()

@app.get('/ping')
def ping_safe(host: str):
    # Safer implementation with proper sanitization
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    subprocess.call(['ping', host])