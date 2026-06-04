from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
import re

app = FastAPI()

@app.get('/ping')
def ping(host: str):
    # Sanitize input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return JSONResponse(content={'error': 'Invalid input'}, status_code=400)
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return JSONResponse(content={'status': 'completed', 'output': result.stdout}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'error': str(e)}, status_code=500)