from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host format')
    # Secure implementation
    subprocess.run(['/bin/ping', host], check=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return {'status': 'completed'}