from fastapi import FastAPI
import subprocess
import shlex
import re
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    # Validate input using regex to allow only alphanumeric characters and hyphens
    if not re.match(r'^[a-zA-Z0-9-]+$', host):
        return {"status": "error", "message": "Invalid host format"}
    args = shlex.split(f"ping {host}")
    subprocess.call(args)
    return {"status": "completed"}