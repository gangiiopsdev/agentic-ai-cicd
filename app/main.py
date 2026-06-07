from fastapi import FastAPI
import subprocess
import shlex

class SafeSubprocess:
    @staticmethod
def call(command: str, *args, **kwargs):
        # Split the command into a list of arguments using shell=True and pass through shlex.split
        cmd = shlex.split(command)
        return subprocess.call(cmd, *args, **kwargs)

app = FastAPI()

def ping(host: str):
    # Safe implementation
    safe_command = 'ping ' + host
    SafeSubprocess.call(safe_command)

@app.get("/ping")
def ping_route(host: str):
    return ping(host)