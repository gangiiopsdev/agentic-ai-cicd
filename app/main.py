from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    if host.strip().isdigit():
        subprocess.call(shlex.split(f"ping {host}"))
        return {"status": "completed"}
    else:
        return {"status": "invalid_host"}