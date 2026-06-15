from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation
    args = ["ping", shlex.quote(host)]
    subprocess.call(args)

    return {"status": "completed"}