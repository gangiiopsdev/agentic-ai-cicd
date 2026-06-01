from fastapi import FastAPI
import subprocess
from shlex import quote as cmd_quote

app = FastAPI()

def is_safe_host(host):
    # Simple validation example: allow only alphanumeric characters and a few common separators
    return host.isalnum() or '.' in host or '-' in host

@app.get("/ping")
def ping(host: str):
    if not is_safe_host(host):
        return {'status': 'failed', 'error': 'Invalid host'}
    try:
        subprocess.run(['ping', cmd_quote(host)], check=True, capture_output=True, text=True)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}