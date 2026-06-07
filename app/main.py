from fastapi import FastAPI
import shlex
import subprocess
global app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    escaped_host = shlex.quote(host)
    subprocess.call(['ping', escaped_host], shell=False)
    return {"status": "completed"}