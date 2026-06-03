from fastapi import FastAPI, HTTPException
import subprocess

app = FastAPI()

def safe_ping(host):
    if not host:
        raise ValueError("Host cannot be empty")
    # Sanitize the input before using it in subprocess
    sanitized_host = ''.join(e for e in host if e.isalnum() or e in ['-', '.'])
    subprocess.call(['ping', sanitized_host])

@app.get="/ping")
def ping(host: str):
    try:
        return {"status": "completed", "output": safe_ping(host)}
    except ValueError as e:
        return {"error": str(e), "status": "failed"}