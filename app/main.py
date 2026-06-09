from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def safe_ping(host: str):
    # Validate input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')

    args = ['ping', host]
    subprocess.run(args, check=True)

@app.get('/ping')
def ping(host: str):
    safe_ping(host)

    return {'status': 'completed'}