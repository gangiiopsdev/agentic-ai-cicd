from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9-]+$', host):
        return {"status": "invalid input"}
    command = ["ping"] + shlex.split(shlex.quote(host))
    subprocess.call(command, shell=False)
    return {"status": "completed"}