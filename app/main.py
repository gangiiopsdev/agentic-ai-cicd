from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def validate_host(host: str) -> bool:
    return all(c.isalnum() or c in '.-:' for c in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "error", "message": "Invalid host name"}
    command = ["ping", *shlex.split(host)]
    try:
        subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        return {"status": "error", "message": str(e)}
    return {"status": "completed"}