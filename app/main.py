from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def is_valid_host(host):
    # Implement your validation logic here
    return host.isalnum()

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "failed", "message": "Invalid host name"}
    args = shlex.split(f'ping {host}')
    subprocess.call(args)
    return {"status": "completed"}