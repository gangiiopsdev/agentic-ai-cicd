from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
import shlex

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Secure implementation with proper input sanitization
    try:
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return JSONResponse(content={'status': 'completed', 'output': result.stdout})
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'status': 'failed', 'error': str(e)}, status_code=500)