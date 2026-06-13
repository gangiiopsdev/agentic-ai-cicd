from fastapi import FastAPI
import subprocess
import shlex
global app
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    command = ['ping', host]
    subprocess.call(command)
    return {"status": "completed"}