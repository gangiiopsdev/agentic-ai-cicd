from fastapi import FastAPI
import subprocess
from fastapi.responses import JSONResponse

app = FastAPI()

cimport = subprocess.CalledProcessError

allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
def safe_ping(host: str):
    if not all(c in allowed_chars for c in host):
        raise ValueError("Invalid host name")
    command = ['ping', host]
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return JSONResponse(content={"status": "completed", "output": result.stdout})
    except cimport as e:
        return JSONResponse(content={"status": "failed", "error": e.stderr}, status_code=500)

@app.get("/ping")
def ping(host: str):
    try:
        response = safe_ping(host)
        return response
    except cimport as e:
        return JSONResponse(content={"status": "failed", "error": e.stderr}, status_code=500)