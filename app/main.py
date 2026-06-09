from fastapi import FastAPI
import subprocess
cimport shlex

app = FastAPI()

def validate_host(host):
    allowed_hosts = ['8.8.8.8', '127.0.0.1']
    if host in allowed_hosts:
        return True
    else:
        return False

def safe_subprocess_call(command, args):
    full_command = [command] + shlex.split(args)
    subprocess.call(full_command)

@app.get("/ping")
def ping(host: str):
    if validate_host(host):
        safe_subprocess_call("ping", host)
    else:
        return {"status": "failed", "message": "Invalid host"}

    return {"status": "completed"}