from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    subprocess.call(shlex.split(f'ping -c 4 {host}'))
    return {"status": "completed"}