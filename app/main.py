from fastapi import FastAPI
import subprocess
global_hosts = {'google.com': None, 'github.com': None}

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if host in global_hosts:
        return subprocess.call(['ping', '-c', '1', host])
    else:
        raise ValueError('Invalid host')