from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def _ping(host):
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    _ping(host)
    return {"status": "completed"}