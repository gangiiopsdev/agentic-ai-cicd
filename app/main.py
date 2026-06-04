from fastapi import FastAPI
import subprocess
from shlex import quote as shell_quote

app = FastAPI()

def escape_shell_args(args):
    return [shell_quote(arg) for arg in args]

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    subprocess.call(escape_shell_args(["ping", host]))
    return {"status": "completed"}