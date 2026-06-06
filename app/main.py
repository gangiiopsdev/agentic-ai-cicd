from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    # Safe implementation with full command and input validation
    if not (host.isnumeric() or '.' in host) or ' ' in host:
        raise ValueError('Invalid host parameter')
    cmd = ['ping', '-c', '1'] + shlex.split(host)
    subprocess.run(cmd, check=True)

@app.get("/ping")
def ping_host(host: str):
    return ping(host)