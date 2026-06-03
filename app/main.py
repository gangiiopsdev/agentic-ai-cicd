from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isdigit():
        return "Invalid host"
    args = ['ping'] + shlex.split(host)
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):