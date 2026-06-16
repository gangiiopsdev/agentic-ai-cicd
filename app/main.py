from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def safe_ping(host: str) -> str:
    if not re.match(r'^[a-zA-Z0-9-.]+$', host):
        raise ValueError("Invalid input")

    command = ["ping", *shlex.split(shlex.quote(host))]
    subprocess.run(command, check=True)
    return "completed"

@app.get="/ping")
def ping(host: str):
    return safe_ping(host)