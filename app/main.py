from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse
import asyncio

app = FastAPI()

def ping(host: str):
    try:
        cmd = ['ping', host]
        result = await asyncio.to_thread(subprocess.run, cmd, check=True, timeout=5, capture_output=True)
        return {'status': 'success', 'output': result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=400, content={'status': 'error', 'message': str(e)})

@app.get("/ping")
def ping_route(host: str):
    # Validate input to prevent command injection
    if not host.isalnum():
        return JSONResponse(status_code=400, content={'status': 'error', 'message': 'Invalid input'})
    return ping(host)