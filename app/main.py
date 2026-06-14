from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    args = ['ping', host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid host name')
    safe_host = shlex.quote(host)
    args = ['ping', '-c', '1', safe_host]
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout