from fastapi import FastAPI
import shlex
from fastapi.responses import JSONResponse
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        args = shlex.split(f'ping {sanitized_host}')
        result = subprocess.run(args, check=True, capture_output=True, text=True)
        return JSONResponse(content={"status": "completed", "output": result.stdout}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)