from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    command_parts = shlex.split(f'ping {host}')
    subprocess.run(command_parts, check=True)

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}