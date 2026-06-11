from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    if host == 'localhost' or host.startswith('127.0.0.1'):
        # Allow local pings only
        subprocess.call(['ping', host])  # Use list instead of shell=True and shlex.split
    else:
        raise ValueError('Invalid host for ping operation')

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}