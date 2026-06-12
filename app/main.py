from fastapi import FastAPI
import subprocess
from shlex import quote
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    if not host.isalnum() or '.' not in host:
        return JSONResponse(status_code=400, content={'status': 'failed', 'error': 'Invalid host'})
    try:
        output = subprocess.check_output(['ping', quote(f'@{host}'), '-c', '1'], stderr=subprocess.STDOUT, timeout=5)
        return JSONResponse(content={'status': 'completed', 'output': output.decode('utf-8')})
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={'status': 'failed', 'error': e.output.decode('utf-8')})