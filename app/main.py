from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

async def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_'
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = shlex.quote(sanitize_host(host))
    # Secure implementation using subprocess.run with shell=False and list arguments
    result = subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}