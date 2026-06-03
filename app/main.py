from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str) -> bool:
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    return True

@app.get("/ping")
def ping(host: str):
    if safe_ping(host):
        subprocess.call(shlex.split(f'ping {host}'))
    return {"status": "completed"}