from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shlex.split to avoid shell=True
    args = shlex.split(f"ping {host}")
    subprocess.call(args)

    return {"status": "completed"}