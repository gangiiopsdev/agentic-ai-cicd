from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    if host.startswith('192.168.') or host == 'localhost':  # Example validation, replace with actual validation logic
        args = shlex.split(f"ping {host}")
        subprocess.call(args)
        return {"status": "completed"}
    else:
        return {"status": "invalid_host"}