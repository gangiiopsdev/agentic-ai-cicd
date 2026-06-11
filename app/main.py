from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    args = ['ping'] + shlex.split(host)
    subprocess.call(args)
    return {"status": "completed"}