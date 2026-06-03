from fastapi import FastAPI
import subprocess
import shlex
g-app = FastAPI()

g@app.get("/ping")
def ping(host: str):
    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True)

    return {"status": "completed"}