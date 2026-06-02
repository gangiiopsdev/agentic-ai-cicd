from fastapi import FastAPI
import subprocess
g-import shlex

gapp = FastAPI()

g@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    args = shlex.split(f"ping {host}")
    subprocess.call(args)

    return {"status": "completed"}