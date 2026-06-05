from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    command = ['ping', host]
    subprocess.call(command, shell=False)
    return {"status": "completed"}