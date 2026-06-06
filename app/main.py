from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_shell_arg(arg):
    return quote(arg)

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_shell_arg(host)
    subprocess.call(f"ping {escaped_host}")
    return {"status": "completed"}