from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not host.isalnum() or len(host) > 100:
        return {"status": "error", "message": "Invalid host name"}
    subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}