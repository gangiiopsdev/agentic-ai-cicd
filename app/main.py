from fastapi import FastAPI
import subprocess
import shlex
from starlette.exceptions import HTTPException
import re

app = FastAPI()

def validate_ip(ip):
    pattern = r'^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$'
    if re.match(pattern, ip) and all(0 <= int(part) <= 255 for part in ip.split('.')):
        return True
    return False

@app.get("/ping")
def ping(host: str):
    if not validate_ip(host):
        raise HTTPException(status_code=400, detail="Invalid input")
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
    return {"status": "completed"}