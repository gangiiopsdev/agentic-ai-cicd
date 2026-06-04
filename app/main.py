from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Safe implementation using shlex
    cmd = ['ping', host]
    subprocess.call(cmd, shell=False)
    return {"status": "completed"}