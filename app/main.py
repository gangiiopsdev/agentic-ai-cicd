from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

# Improved regex pattern to match valid hostnames/IP addresses
HOST_PATTERN = r'^[a-zA-Z0-9.-]{1,255}$'

def validate_host(host):
    return re.match(HOST_PATTERN, host) is not None

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"status": "failed", "error": "Invalid input"}
    try:
        output = subprocess.run(shlex.split(f'ping {host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "output": output.stdout.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr.decode()}