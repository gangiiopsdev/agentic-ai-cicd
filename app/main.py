from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Fixed implementation
    subprocess.call(shlex.split(f'ping {host}'))

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)