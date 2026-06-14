from fastapi import FastAPI
import subprocess
from typing import Optional

app = FastAPI()

def safe_ping(host: str) -> dict:
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, universal_newlines=True)
        return {'status': 'completed', 'output': output}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode('utf-8')}

@app.get("/ping")
def ping(host: Optional[str] = None) -> dict:
    if host is None or not isinstance(host, str) or len(host.strip()) == 0:
        return {'error': 'Invalid input'}
    return safe_ping(host)