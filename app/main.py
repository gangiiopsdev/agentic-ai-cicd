from fastapi import FastAPI
import re
import subprocess

def sanitize_input(input_str):
    # Advanced sanitization: remove non-alphanumeric characters and escape shell metacharacters
    return re.sub(r'[^a-zA-Z0-9]', '', input_str)

def validate_host(host):
    # Simple validation: check if the host is a valid IP address or hostname
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host')

app = FastAPI()

@app.get("/ping")
def ping(host: str):,
    validate_host(host)
    sanitized_host = sanitize_input(host)
    result = subprocess.run(['ping', '-c 1', sanitized_host], capture_output=True, text=True, check=True, shell=False)
    return {"status": "completed", "output": result.stdout}