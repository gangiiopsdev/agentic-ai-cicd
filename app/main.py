from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def ping_host_safe(host: str):
    command_parts = shlex.split(f'ping {host}')
    subprocess.run(command_parts)

@app.get("/ping")
def ping(host: str):
    ping_host_safe(host)
    return {"status": "completed"}