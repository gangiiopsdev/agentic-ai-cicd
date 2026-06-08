from fastapi import FastAPI
import subprocess
import re
def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '-.')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not re.match(r'^[a-zA-Z0-9]+-[a-zA-Z0-9]+$', sanitized_host):
        return {'status': 'failed', 'error': 'Invalid host name'}
    try:
        args = ['ping', subprocess.quote(sanitized_host)]  # Use subprocess.quote to safely include the host in the command
        result = subprocess.run(args, capture_output=True, text=True, check=False)
        if result.returncode != 0:
            raise subprocess.CalledProcessError(result.returncode, args, output=result.stdout, stderr=result.stderr)
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}
    return {'status': 'completed'}