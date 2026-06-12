from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    if not host.isalnum():
        return False
    return True

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"error": "Invalid input"}
    subprocess.run(shlex.split(f'ping -c 1 {host}'), check=True)
    return {"status": "completed"}