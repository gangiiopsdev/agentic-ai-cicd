from fastapi import FastAPI
import subprocess
from typing import Optional
from shlex import quote

app = FastAPI()

def sanitize_input(input_str: str) -> str:
    return ''.join(filter(str.isalnum, input_str))

@app.get("/ping")
def ping(host: Optional[str] = None):
    if host is None or not host.strip():
        return {'status': 'failed', 'error': 'Invalid input'}
    sanitized_host = sanitize_input(host)
    try:
        output = subprocess.run(['ping', '-c 1', quote(sanitized_host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}