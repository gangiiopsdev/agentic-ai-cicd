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
        output = subprocess.check_output(['ping', '-c 1', quote(sanitized_host)], stderr=subprocess.STDOUT, text=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output}