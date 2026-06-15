from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
import shlex

app = FastAPI()

def validate_host(host):
    if not host.strip():
        raise ValueError('Host cannot be empty')
    for char in host:
        if not (char.isalnum() or char in ['.', '-', '_']):
            raise ValueError('Invalid character in host name')

@app.get('/ping')
def ping(host: str):
    validate_host(host)
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return JSONResponse(content={'status': 'completed', 'output': result.stdout})
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'status': 'failed', 'error': str(e)}, status_code=500)