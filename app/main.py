from fastapi import FastAPI
import subprocess
import shlex
type hinting and from typing import Optional

app = FastAPI()

@app.get('/ping')
def ping(host: Optional[str] = None):
    if not host:
        return {'status': 'failed', 'error': 'Host parameter is required'}
    try:
        result = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': str(e)}