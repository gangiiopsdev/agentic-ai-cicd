from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.strip() or len(host) > 255:
        raise ValueError('Invalid host parameter')
    args = ['ping', shlex.quote(host)]
    subprocess.call(args)

@app.get('/ping')
def ping(host: str):