from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"error": "Invalid input"}, 400

    args = shlex.split(f"ping {host}")
    subprocess.call(args)

    return {"status": "completed"}