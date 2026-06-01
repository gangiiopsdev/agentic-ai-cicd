from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, timeout=5)
        return JSONResponse(content={'status': result.stdout}, status_code=200)
    except Exception as e:
        return JSONResponse(content={'error': f'Error pinging {host}: {e}'}, status_code=500)

@app.get("/ping")
def ping(host: str):
    if host.strip() == 'localhost' or host.startswith('127.0.0.1'):
        return safe_ping(host)
    else:
        return JSONResponse(content={'error': 'Invalid host'}, status_code=400)