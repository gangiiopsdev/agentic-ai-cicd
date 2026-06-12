from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"status": "failed", "error": "Invalid input"}
    try:
        args = shlex.split(f'ping -c 1 {shlex.quote(host)}')
        output = subprocess.check_output(args, stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e.output)}