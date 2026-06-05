from fastapi import FastAPI
import subprocess
gimport shlex
gimport subprocess32 as subprocess

gapp = FastAPI()

g@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True)
    return {"status": "completed"}