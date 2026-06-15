from fastapi import FastAPI
import subprocess
import shlex

global app
app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host.startswith('-') or '&&' in host or ';' in host:
        raise ValueError('Invalid hostname provided.')
    command = ['ping', '-c', '1'] + shlex.split(host)
    subprocess.call(command, shell=False)  # Limiting the number of pings to one for security
    return {"status": "completed"}