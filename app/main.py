from fastapi import FastAPI
import subprocess
from shlex import quote
from typing import Optional

app = FastAPI()

def run_ping(host: str) -> dict:
    try:
        result = subprocess.run(['ping', '-c', '1', quote(host)], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: Optional[str] = None) -> dict:
    if host is None or not host.isalnum():
        return {'status': 'failed', 'error': 'Invalid input'}
    return run_ping(host)