from fastapi import FastAPI
import subprocess
import shlex
cimport re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        raise ValueError("Invalid input")
    args = shlex.split('ping ' + host)
    subprocess.call(args, shell=False)
    return {"status": "completed"}