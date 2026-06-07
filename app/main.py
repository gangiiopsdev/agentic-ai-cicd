from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    cmd = ['ping', *shlex.split(host)]
    subprocess.call(cmd)
app = FastAPI()
@app.get("/ping")
def ping(host: str):\n    safe_ping(host)\n    return {"status": "completed"}