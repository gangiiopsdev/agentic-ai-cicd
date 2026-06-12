from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def sanitize_host(host: str) -> str:
    if not host.isalnum() or len(host) > 10:
        raise ValueError("Invalid input")
    return host

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    command = shlex.split('ping ' + sanitized_host)
    subprocess.call(command, shell=False)
    return {"status": "completed"}