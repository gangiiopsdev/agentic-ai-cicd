from fastapi import FastAPI
import subprocess
import shlex
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return JSONResponse(content={'status': 'completed', 'output': result.stdout}, status_code=200)
    except Exception as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)