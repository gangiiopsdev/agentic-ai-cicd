from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

def safe_ping(host):
    # Safe implementation using subprocess.run with shlex.split and shell=False
    args = ['ping', host]
    subprocess.run(args, check=True, shell=False)

@app.get("/ping")
def ping(host: str):
    safe_ping(shlex.quote(host))
    return {"status": "completed"}