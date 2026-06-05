from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if 'ping' in host or '--' in host:
        raise ValueError('Invalid input detected')
    command = ["ping", *shlex.split(host)]
    subprocess.call(command)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}