from fastapi import FastAPI
import subprocess
import shlex
def is_valid_host(host: str) -> bool:
    allowed_hosts = ["example.com", "test.example.com"]
    return host in allowed_hosts
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host")
    subprocess.run(shlex.split(f'ping {host}'), check=True)
    return {"status": "completed"}