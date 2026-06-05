from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safer implementation using shlex to safely split the command arguments
    args = ['ping'] + shlex.split(host)
    subprocess.call(args, shell=False)
    return {"status": "completed"}