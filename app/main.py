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
    # Use subprocess.run for better control and to avoid shell injection risks
    try:
        result = subprocess.run(['ping', '-c', '1', safe_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Error pinging host: {e.stderr.decode('utf-8')}")