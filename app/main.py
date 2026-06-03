from fastapi import FastAPI
import subprocess
import shlex
gapp = FastAPI()

def safe_ping(host: str):
    args = ['ping', host]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}