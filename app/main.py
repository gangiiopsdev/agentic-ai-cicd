from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "invalid input"}
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed"}