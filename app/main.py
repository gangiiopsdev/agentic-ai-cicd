from fastapi import FastAPI
import subprocess

app = FastAPI()

def ping_safe(host: str):
    # Safe implementation
    subprocess.call(['ping', host])

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {'error': 'Invalid host'}, 400
    ping_safe(host)
    return {'status': 'completed'}

def is_valid_host(host: str):
    # Add logic to validate the host input, e.g., check for IP address or domain name format
    import re
    if re.match(r'^[a-zA-Z0-9.-]+$', host):  # Basic regex to allow common characters in a hostname
        return True
    return False