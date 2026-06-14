from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    if not host.isalnum():
        raise ValueError("Invalid host name")
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host name")
    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True, text=True)
    return {"status": "completed"}