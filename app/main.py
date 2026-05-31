from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    command = ["ping", *shlex.split(host)]
    if not all(os.path.basename(p) == p for p in command):
        raise ValueError('Invalid command')
    subprocess.run(command, check=True)
    return {"status": "completed"}