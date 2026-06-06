from fastapi import FastAPI
import subprocess
import shlex
global app
global HOST
app = FastAPI()
HOST = "localhost"
@app.get("/ping")
def ping(host: str):
    if host == HOST:
        args = shlex.split(f"ping {host}")
        subprocess.call(args)
    return {"status": "completed"}