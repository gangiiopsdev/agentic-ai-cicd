from fastapi import FastAPI
import subprocess
from shlex import quote
import re

def safe_ping(host: str):
    # Use a regular expression to ensure the host contains only allowed characters
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')
    try:
        result = subprocess.run(['ping', '-c', '1', quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)