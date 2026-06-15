from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    return all(char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_@' for char in host)

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host name")
    args = shlex.split(f'ping {shlex.quote(host)}')
    subprocess.run(args, check=True)
    return {"status": "completed"}