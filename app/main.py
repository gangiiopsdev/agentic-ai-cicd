from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return shlex.quote(arg)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid host parameter")
    command = ["ping", escape_shell_arg(host)]
    subprocess.run(command, shell=False)
    return {"status": "completed"}