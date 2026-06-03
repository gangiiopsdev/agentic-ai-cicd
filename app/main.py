from fastapi import FastAPI
import shlex
import subprocess

app = FastAPI()

def safe_ping(host):
    # Using shlex.quote to safely escape command arguments
    quoted_host = shlex.quote(host)
    result = subprocess.run(['ping', '-c', '1', quoted_host], capture_output=True, text=True, check=False)
    return {'status': 'completed', 'output': result.stdout}

@app.get('/ping')
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not host.replace('.', '').isalnum():
        return {'error': 'Invalid input'}
    return safe_ping(host)