from fastapi import FastAPI
import subprocess
import shlex
from fastapi.responses import JSONResponse
def sanitize_input(input_string):
    return ''.join(c for c in input_string if c.isalnum() or c == '.')

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_input(host)
    if not sanitized_host:
        return JSONResponse(status_code=400, content={'error': 'Invalid input'})
    try:
        args = ['ping'] + shlex.split(sanitized_host)
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return JSONResponse({'status': 'completed', 'output': output.decode()})
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=400, content={'error': e.output.decode()})
    except subprocess.TimeoutExpired:
        return JSONResponse(status_code=408, content={'message': 'Ping request timed out'})