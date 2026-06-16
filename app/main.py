from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    args = ['ping', host]
    # Validate the host parameter to ensure it does not contain malicious input
    if not validate_host(host):
        return {'status': 'error', 'message': 'Invalid host'}
    subprocess.call(args)
    return {'status': 'completed'}
def validate_host(host: str) -> bool:
    # Implement a simple validation function to check for valid IP addresses or domain names
    import re
    if re.match(r'^[a-zA-Z0-9.-]+$', host):
        return True
    return False