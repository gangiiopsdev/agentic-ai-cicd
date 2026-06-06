from fastapi import FastAPI
import subprocess
import shlex
import re
def validate_host(host):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    if not all(c in allowed_chars for c in host):
        raise ValueError("Invalid characters in host")
    # Ensure the host does not contain any executable commands
    if re.search(r'[^a-zA-Z0-9.-]', host, re.IGNORECASE):
        raise ValueError("Host contains executable characters")

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    safe_host = shlex.quote(host)
    # Use subprocess.Popen instead of subprocess.run for better control
    process = subprocess.Popen(['ping', '-c', '1', safe_host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    if process.returncode != 0:
        raise RuntimeError(f"Error pinging host: {error.decode('utf-8')}")
    return {'status': 'completed'}