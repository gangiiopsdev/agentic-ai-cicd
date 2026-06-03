from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

def safe_ping(host: str):
    if not all(c in allowed_chars for c in host):
        raise ValueError("Invalid host name")
    command = ['ping', host]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        return JSONResponse(content={"status": "completed", "output": result.stdout})
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"status": "failed", "error": str(e.stderr)}, status_code=500)

app = FastAPI()
cimport = subprocess.CalledProcessError
allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return response
    except cimport as e:
        return JSONResponse(content={"status": "failed", "error": str(e.stderr)}, status_code=500)