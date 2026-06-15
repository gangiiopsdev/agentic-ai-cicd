from fastapi import FastAPI
import subprocess
import shlex
from starlette.exceptions import HTTPException
global app
app = FastAPI()

def validate_host(host):
    try:
        int(host)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid input")

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    args = shlex.split(f'ping {host}')
    result = subprocess.run(args, capture_output=True, text=True, check=False)
    if result.returncode != 0:
        raise HTTPException(status_code=500, detail=result.stderr.strip())
    return {"status": "completed", "output": result.stdout.strip()}