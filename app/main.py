from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host: str) -> bool:
    return host.isalnum()

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        raise ValueError("Invalid host name")
    command = shlex.split(f"ping {host}")
    subprocess.run(command, check=True)
    return {"status": "completed"}