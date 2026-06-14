from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    safe_host = shlex.quote(host)
    subprocess.call(f'ping {safe_host}')

@app.get("/ping")
def ping_route(host: str):
    return ping(host)