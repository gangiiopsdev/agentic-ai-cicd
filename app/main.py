from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = shlex.quote(host)
    try:
        output = subprocess.run(["ping", *shlex.split(safe_host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "result": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "error", "result": str(e)}