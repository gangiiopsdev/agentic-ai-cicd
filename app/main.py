from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize host input
    if not host.isalnum() or len(host) > 255:
        raise ValueError("Invalid host name")
    subprocess.run(['ping', shlex.quote(host)], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
    return {"status": "completed"}