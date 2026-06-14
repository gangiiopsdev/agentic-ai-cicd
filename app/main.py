from fastapi import FastAPI
import subprocess
import shlex
from starlette.exceptions import HTTPException

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isdigit():
        raise HTTPException(status_code=400, detail="Invalid input")
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}