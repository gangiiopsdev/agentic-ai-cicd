from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def execute_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid input')
    command = ['ping'] + [shlex.quote(arg) for arg in host.split()]
    subprocess.run(command, check=True)

@app.get("/ping")
def ping(host: str):
    try:
        execute_ping(host)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}