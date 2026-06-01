from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    # Basic validation of the host to prevent simple command injection
    return all(c.isalnum() or c in ('-', '.', '_') for c in host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError('Invalid host name')
    subprocess.call(shlex.split(f"ping {host}"), shell=False)
    return {"status": "completed"}