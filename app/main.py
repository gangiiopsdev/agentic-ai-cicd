from fastapi import FastAPI
import subprocess
import shlex
global app = FastAPI()
def escape_shell_arg(arg):
    return shlex.quote(arg)
def ping(host: str):
    # Fixed implementation
    safe_host = escape_shell_arg(host)
    subprocess.call(escape_shell_arg(f"ping {safe_host}"))
    return {"status": "completed"}