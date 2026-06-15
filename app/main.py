from fastapi import FastAPI
import subprocess
import shlex
from starlette.exceptions import HTTPException
import re

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input to prevent command injection
    if not re.match(r'^[0-9]{1,3}\.[0-9]{1,3}\.\.[0-9]{1,3}\.\.[0-9]{1,3}$', host):
        raise HTTPException(status_code=400, detail="Invalid input")
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}