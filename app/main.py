from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid host name")
    command = ["ping", shlex.quote(host)]
    subprocess.call(command, shell=False)

@app.get="/ping")
def ping(host: str):
    return safe_ping(host)