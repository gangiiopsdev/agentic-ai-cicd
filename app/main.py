from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not host.isalnum() and '-' not in host:
        return {"status": "invalid input"}
    command = ["ping"] + shlex.split(host)
    subprocess.call(command, shell=False)
    return {"status": "completed"}