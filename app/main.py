from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def secure_ping(host: str):
    if not host.isalnum():
        raise ValueError("Invalid input")
    command_parts = shlex.split(f'ping {host}')
    subprocess.call(command_parts)

@app.get="/ping")
def ping(host: str):
    return secure_ping(host)