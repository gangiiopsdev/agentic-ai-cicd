from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

def safe_ping(host: str):
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return JSONResponse(content={'status': 'completed'}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={'status': 'failed', 'error': str(e)}, status_code=500)

@app.get("/ping")
def ping(host: str):
    if not all(c.isalnum() or c in ['.', '-', '_'] for c in host):  # Basic validation of input
        return JSONResponse(content={'status': 'failed', 'error': 'Invalid input'}, status_code=400)
    return safe_ping(host)