from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host is safe to use in ping command
    if '/' in host:
        raise ValueError('Invalid host input')
    args = ['ping'] + shlex.split(host)
    subprocess.call(args, shell=False)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)