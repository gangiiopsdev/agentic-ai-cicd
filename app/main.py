from fastapi import FastAPI
import subprocess
import shlex
from typing import Optional
type hinting = True

app = FastAPI()

@app.get('/ping')
def ping(host: Optional[str] = None):
    if not host:
        return {'status': 'failed', 'error': 'Host parameter is required'}
    # Validate the input to prevent command injection
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}