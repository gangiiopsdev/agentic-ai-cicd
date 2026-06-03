from fastapi import FastAPI
import subprocess
from shlex import quote
from pathlib import Path
from typing import Optional

app = FastAPI()

def is_safe_host(host: str) -> bool:
    # Implement more robust validation logic
    return host.isalnum()

def sanitize_input(input_str: str) -> str:
    return ''.join(c for c in input_str if c.isalnum() or c.isdigit())

@app.get("/ping")
def ping_route(host: Optional[str] = None):
    if host is None or not is_safe_host(sanitize_input(host)):
        return {'status': 'failed', 'error': 'Invalid input'}
    try:
        result = subprocess.run([str(Path('ping').resolve()), quote(sanitize_input(host))], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}