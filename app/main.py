from fastapi import FastAPI
import subprocess
import shlex
def _ping(host):
    args = ['ping', '-c', '1', shlex.quote(host)]
    subprocess.call(args)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    _ping(host)
    return {"status": "completed"}