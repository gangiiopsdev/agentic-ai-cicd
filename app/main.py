from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def create_subprocess(command):
    args = shlex.split(command)
    return subprocess.Popen(args)

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    process = create_subprocess(command)
    process.wait()

    return {"status": "completed"}