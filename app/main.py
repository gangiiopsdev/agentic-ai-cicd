from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '')

@app.get("/ping")
def ping(host: str):
    # Secure implementation using shell=False and list of arguments
    args = shlex.split(host)
    subprocess.call(['ping'] + args)
    return {"status": "completed"}