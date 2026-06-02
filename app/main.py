from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    if not host.isalnum() or '.' not in host:
        raise ValueError("Invalid host")
    args = shlex.split(f"ping {host}")
    subprocess.run(args, check=True)

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)