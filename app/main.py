from fastapi import FastAPI
import subprocess
import re
from shlex import quote

app = FastAPI()

def is_valid_host(host):
    pattern = r'^([a-zA-Z0-9]([a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$'
    return re.match(pattern, host) is not None

def execute_command(command):
    subprocess.run(command, check=True)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host address")
    execute_command(['ping', quote(host)])
    return {"status": "completed"}