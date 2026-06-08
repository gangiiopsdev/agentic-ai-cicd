from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping(host: str):
    if not host.strip():
        raise ValueError('Invalid host')
    args = ['ping', shlex.quote(host)]
    subprocess.run(args, capture_output=True, text=True)

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)