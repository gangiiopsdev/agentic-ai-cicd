from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess_call(command, args):
    full_command = [command] + list(shlex.split(args))
    subprocess.call(full_command)

@app.get("/ping")
def ping(host: str):
    allowed_hosts = ['localhost', '127.0.0.1']  # Add more allowed hosts as needed
    if host.strip() in allowed_hosts:
        safe_subprocess_call('ping', host)
        return {"status": "completed"}
    else:
        return {"status": "error", "message": "Invalid host"}