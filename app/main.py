from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = escape_shell_arg(host)
    command = ['ping', safe_host]
    subprocess.run(command, check=True)
    return {"status": "completed"}