from fastapi import FastAPI
import shlex
import subprocess

global app = FastAPI()

def safe_ping(host: str):
    # Safe implementation using shlex.quote
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    return {'result': safe_ping(host)}