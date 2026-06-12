from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Ensure the host input does not contain malicious content
    if 'ping' not in host:
        return "Invalid command"
    cmd = ['ping'] + shlex.split(host)
    subprocess.call(cmd, shell=False)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)