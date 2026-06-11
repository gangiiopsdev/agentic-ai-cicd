from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    args = shlex.split(f"ping {host}")
    subprocess.call(args)
    return {"status": "completed"}