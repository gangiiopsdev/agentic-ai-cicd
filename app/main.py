from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def validate_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    if not all(c in allowed_chars for c in host):
        raise ValueError("Invalid characters in host")
    # Ensure the host does not contain any executable commands
    if re.search(r'[^a-zA-Z0-9.-]', host, re.IGNORECASE):
        raise ValueError("Host contains executable characters")

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    safe_host = shlex.quote(host)
    subprocess.run(['ping', '-c', '1', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return {'status': 'completed'}