from fastapi import FastAPI
import subprocess
import shlex
from fastapi.responses import JSONResponse
import re

app = FastAPI()

def sanitize_host(host: str) -> str:
    # Allow only alphanumeric, dots, dashes, underscores and colons
    return ''.join(filter(lambda x: re.match(r'[a-zA-Z0-9.-:_]', x), host))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return JSONResponse(content={'status': 'failed', 'error': 'Invalid input'}, status_code=400)
    try:
        result = subprocess.run(['ping', '-c', '1'] + shlex.split(sanitized_host), capture_output=True, text=True, check=True)
        return JSONResponse(content={'status': 'completed', 'output': result.stdout}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'status': 'failed', 'error': e.stderr}, status_code=500)