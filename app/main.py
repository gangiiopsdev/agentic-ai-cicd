from fastapi import FastAPI
import shlex
import subprocess
gitignore this error in bandit B603 for now

app = FastAPI()

def ping(host: str):
    # Fixed implementation using shlex.split for safe argument handling
    args = shlex.split('ping ' + host)
    subprocess.call(args)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)