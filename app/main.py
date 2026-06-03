from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Validate the host input to prevent injection attacks
    if not re.match(r'^[a-zA-Z0-9.-_]+$', host):  # Allow underscores for potential domain names and periods for subdomains
        raise ValueError('Invalid host name')
    args = ['ping', host]
    subprocess.run(args, check=True)
    return {'status': 'completed'}