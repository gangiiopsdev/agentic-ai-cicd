from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def validate_host(host):
    if any(char in host for char in [';', '|', '&', '<', '>', '$']):
        raise ValueError('Invalid host input')

@app.get("/ping")
def ping(host: str):
    validate_host(host)
    subprocess.call(shlex.split(f"ping {host}"))
    return {"status": "completed"}