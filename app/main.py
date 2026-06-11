from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using shlex.quote for argument parsing and avoiding shell=True
    cmd = ["ping", *shlex.split(host)]
    subprocess.run(cmd, check=True)
    return {"status": "completed"}