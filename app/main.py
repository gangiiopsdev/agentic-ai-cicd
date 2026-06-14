from fastapi import FastAPI, HTTPException
import re
import subprocess

app = FastAPI()

def sanitize_hostname(hostname):
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(c for c in hostname if c in allowed_chars)

@app.get('/ping')
def ping(host: str):
    sanitized_host = sanitize_hostname(host)
    if not re.match(r'^[a-zA-Z0-9]{1,255}$', sanitized_host):
        raise HTTPException(status_code=400, detail="Invalid hostname")
    result = subprocess.run(['ping', '-c', '1', sanitized_host], capture_output=True, text=True, check=False)
    return {
        "status": "completed",
        "output": result.stdout if result.returncode == 0 else result.stderr
    }