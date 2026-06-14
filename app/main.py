from fastapi import FastAPI
import subprocess
import shlex
from fastapi.responses import JSONResponse

app = FastAPI()

def sanitize_host(host: str) -> str:
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-:_'
    return ''.join(filter(lambda x: x in allowed_chars, host))

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return JSONResponse(content={'status': 'failed', 'error': 'Invalid input'}, status_code=400)
    try:
        result = subprocess.run(['ping', '-c', '1'] + shlex.split(f'/bin/ping {sanitized_host}'), capture_output=True, text=True, check=True)
        return JSONResponse(content={'status': 'completed', 'output': result.stdout}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'status': 'failed', 'error': e.stderr}, status_code=500)