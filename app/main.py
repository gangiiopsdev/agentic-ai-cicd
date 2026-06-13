from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if host.strip().isnumeric() or '.' in host:
        subprocess.call(shlex.split('ping ' + host))
    else:
        raise ValueError('Invalid host')

@app.get("/ping")
def ping(host: str):