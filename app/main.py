from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def escape_shell_arg(arg):
    return shlex.quote(arg)

def ping(host: str):
    # Fixed implementation
    subprocess.call(escape_shell_arg(f"ping {host}"))
    return {"status": "completed"}