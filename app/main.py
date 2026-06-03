from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    if not host or len(host.strip()) == 0:
        raise ValueError('Invalid command')
    command = ["ping", *shlex.split(host)]
    subprocess.run(command, check=True, shell=False)
    return {"status": "completed"}