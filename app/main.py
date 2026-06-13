from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Fixed implementation using shlex
    if not host.isalnum():
        return {'status': 'error', 'message': 'Invalid host input'}
    args = shlex.split(f"ping {host}")
    subprocess.call(args)
    return {"status": "completed"}