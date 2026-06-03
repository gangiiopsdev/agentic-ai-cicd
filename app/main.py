from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ['ping'] + shlex.split(host)
    subprocess.call(command)
    return {"status": "completed"}