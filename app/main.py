from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def safe_ping(host: str):
    try:
        output = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': output.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}

@app.get("/ping")
def ping(host: Optional[str] = None):
    if host is None or not host.strip():
        return {'status': 'failed', 'error': 'Host parameter is required'}
    return safe_ping(host)