from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Validate host input
    allowed_chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-')
    if not all(char in allowed_chars for char in host):
        raise ValueError('Invalid host input')
    # Safe implementation using subprocess.run
    cmd = ['ping', shlex.quote(host)]
    subprocess.run(cmd, check=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    try:
        safe_ping(host)
        return {"status": "completed"}
    except Exception as e:
        return {"error": str(e), "status": "failed"}