from fastapi import FastAPI
import subprocess
import shlex
import re

cmd_regex = re.compile(r'^[a-zA-Z0-9_\s]*$')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if cmd_regex.match(host):
        subprocess.call(shlex.split(f"ping {host}"))
    else:
        return {"error": "Invalid host input"}
    return {"status": "completed"}