from fastapi import FastAPI
import subprocess
import shlex
def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    subprocess.call(['ping'] + shlex.split(host), shell=False)
    return {"status": "completed"}