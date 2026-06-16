from fastapi import FastAPI
import subprocess
from typing import Dict

app = FastAPI()

@app.get('/ping', response_model=Dict[str, str])
def ping(host: str) -> Dict[str, str]:
    if not host.strip():
        return {'status': 'failed', 'error': 'Host parameter is required'}
    try:
        output = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, timeout=5)
        if output.returncode == 0:
            return {'status': 'completed', 'output': output.stdout}
        else:
            return {'status': 'failed', 'error': output.stderr}
    except subprocess.TimeoutExpired:
        return {'status': 'failed', 'error': 'Command timed out'}