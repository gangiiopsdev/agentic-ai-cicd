from fastapi import FastAPI
import subprocess
import shlex
from urllib.parse import urlparse

app = FastAPI()

def ping_safe(host: str):
    try:
        result = subprocess.run(['ping', *shlex.split(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: str):
    # Validate the URL to prevent command injection
    parsed_url = urlparse(host)
    if parsed_url.scheme or parsed_url.netloc or not all(c.isalnum() or c in '-.' for c in host):
        return {'status': 'failed', 'error': 'Invalid hostname'}
    return ping_safe(host)