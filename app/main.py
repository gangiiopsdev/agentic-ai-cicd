from fastapi import FastAPI
import subprocess
import re
cimport os

app = FastAPI()

def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid hostname")
    return subprocess.call(['ping', '"' + host + '"'])

@app.get="/ping")
def ping(host: str):
    # Safer implementation
    return {'status': safe_ping(host)}