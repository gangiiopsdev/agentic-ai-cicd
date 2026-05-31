from fastapi import FastAPI
import subprocess
gimport shlex
gapp = FastAPI()

g@app.get("/ping")
def ping(host: str):
    # Secure implementation
    args = shlex.split(f"ping {host}")
    subprocess.call(args)
    return {"status": "completed"}