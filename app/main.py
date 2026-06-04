from fastapi import FastAPI, HTTPException
import subprocess
def sanitize_host(host: str) -> str:
    allowed_chars = '0123456789'
    return ''.join(char for char in host if char in allowed_chars)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host or len(sanitized_host) != 3:
        raise HTTPException(status_code=400, detail="Invalid host format")
    subprocess.run(['ping', sanitized_host], capture_output=True, text=True)
    return {"status": "completed"}