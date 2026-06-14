from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

async def safe_ping(host: str):
    if 'ping' in host or '--help' in host:
        return JSONResponse(content={'status': 'error', 'result': 'Invalid input'}, status_code=400)
    try:
        output = subprocess.check_output(['ping', '-c', '1', host], stderr=subprocess.STDOUT, timeout=5)
        return JSONResponse(content={'status': 'completed', 'result': output.decode('utf-8')}, status_code=200)
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
        return JSONResponse(content={'status': 'error', 'result': str(e)}, status_code=500)

@app.get("/ping")
def ping(host: str):
    result = await safe_ping(host)
    return result