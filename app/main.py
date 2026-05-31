from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate the host input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid hostname')
    # Safe implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def ping_route(host: str):
    return ping(host)