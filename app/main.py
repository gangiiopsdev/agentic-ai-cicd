from fastapi import FastAPI
import subprocess
from shlex import quote
def safe_ping(host: str):
    try:
        # Use subprocess.run for a safer approach with proper quoting of the host parameter
        cmd = ['ping', quote(host)]
        result = subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {'status': 'completed', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr.decode()}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Add input validation and sanitization
    if not host.isalnum():
        return {'status': 'invalid', 'message': 'Invalid input'}
    sanitized_host = ''.join(c for c in host if c.isalnum() or c.isdigit())
    return await safe_ping(sanitized_host)