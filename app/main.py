from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def escape_shell_arg(arg):
    return subprocess.list2cmdline([arg])

@app.get("/ping")
def ping(host: str):
    command = ['ping', escape_shell_arg(host)]
    subprocess.call(command)
    return {"status": "completed"}