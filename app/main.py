from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def ping(host: str):
    # Safe implementation using subprocess.run with sanitized input
    try:
        safe_host = quote(host)
        result = subprocess.run(['ping', safe_host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}