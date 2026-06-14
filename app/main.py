from fastapi import FastAPI
import subprocess

app = FastAPI()

def sanitize_host(host):
    allowed_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    return ''.join(c for c in host if c in allowed_chars)

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {"status": "error", "output": "Invalid host name"}
    # Safe implementation using subprocess.run with check=True and capturing output
    result = subprocess.run(["/sbin/ping", sanitized_host], capture_output=True, text=True, check=True)  # Use full path for 'ping'
    return {"status": "completed", "output": result.stdout}