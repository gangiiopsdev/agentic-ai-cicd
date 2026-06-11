from fastapi import FastAPI
import subprocess
from fastapi import HTTPException
def sanitize_host(host: str) -> str:
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-')
    return ''.join(char for char in host if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        raise HTTPException(status_code=400, detail="Invalid input")
    try:
        result = subprocess.run(['ping', sanitized_host], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": result.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}