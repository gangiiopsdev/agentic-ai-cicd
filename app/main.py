from fastapi import FastAPI
import subprocess
import shlex
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum():
        return JSONResponse(status_code=400, content={'error': 'Invalid input'})
    try:
        args = ['ping'] + shlex.split(host)
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return JSONResponse({'status': 'completed', 'output': output.decode()})
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=400, content={'error': e.output.decode()})
    except subprocess.TimeoutExpired:
        return JSONResponse(status_code=408, content={'message': 'Ping request timed out'})