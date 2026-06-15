from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host input is sanitized or validated
    if not re.match(r'^[a-zA-Z0-9.,-_ ]+$', host) or len(host.split()) > 1:
        return {'status': 'error', 'message': 'Invalid host name'}
    subprocess.run(['ping', host], check=True)

@app.get('/ping')
def ping(host: str):
    return safe_ping(host)