from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}