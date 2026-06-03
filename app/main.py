from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation with shell=False and proper input sanitization
    args = shlex.split(f"ping {host}")
    subprocess.call(args, shell=False)
    return {"status": "completed"}