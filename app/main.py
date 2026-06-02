from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def escape_command_line_arg(arg):
    return quote(arg)

@app.get("/ping")
def ping(host: str):
    safe_host = escape_command_line_arg(host)
    command = ['ping', safe_host]
    subprocess.run(command, check=True, shell=False)
    return {"status": "completed"}