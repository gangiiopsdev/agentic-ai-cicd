from fastapi import FastAPI
import subprocess
from shlex import quote
from typing import Dict

app = FastAPI()

async def sanitize_input(input_string: str) -> str:
    # Basic sanitization logic to avoid command injection
    return ''.join(c for c in input_string if c.isalnum() or c in '.-')

@app.get('/ping', response_model=Dict[str, str])
def ping(host: str) -> Dict[str, str]:
    sanitized_host = quote(sanitize_input(host))
    try:
        output = subprocess.check_output(['ping', '-c', '1', sanitized_host], stderr=subprocess.STDOUT, timeout=5)
        return {'status': 'completed', 'output': output.decode('utf-8')}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}