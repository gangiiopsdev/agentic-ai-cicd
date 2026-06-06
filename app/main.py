from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        args = ['ping', shlex.quote(host)]
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, timeout=5)
        return JSONResponse(content={'status': 'completed', 'output': output.decode()})
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return JSONResponse(status_code=400, content={'status': 'error', 'message': str(e)})