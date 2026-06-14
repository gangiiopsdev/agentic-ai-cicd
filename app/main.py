from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    try:
        # Use shlex.quote to safely quote the host argument
        result = subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed'}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode('utf-8')}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host and '@' not in host and ':' not in host and '/' not in host:
        # Validate and sanitize the hostname before passing it to the subprocess module
        if all(c.isalnum() or c in '-.' for c in host):
            return safe_ping(host)
        else:
            return {'status': 'failed', 'error': 'Invalid hostname'}
    else:
        return {'status': 'failed', 'error': 'Invalid hostname'}