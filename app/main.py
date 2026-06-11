from fastapi import FastAPI
import subprocess
import shlex
from fastapi.responses import JSONResponse

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    try:
        args = shlex.split(f'ping {sanitized_host}')
        subprocess.run(args, check=True)
        return JSONResponse(content={"status": "completed"}, status_code=200)
    except subprocess.CalledProcessError as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)