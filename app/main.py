from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    args = shlex.split(f"ping {host}")
    subprocess.call(args)
    return {"status": "completed"}