from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def ping(host: str):
    # Validate host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError("Invalid host")
    # Secure implementation using list for args instead of shell=True
    subprocess.call(['ping', host])

@app.get="/ping")
def ping_endpoint(host: str):
    return ping(host)