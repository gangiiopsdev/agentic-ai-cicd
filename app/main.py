from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Define a regex pattern for allowed characters in hostnames/IPs
    pattern = re.compile(r'^[a-zA-Z0-9.-_:@/]*$')
    if pattern.match(host.strip()):
        subprocess.call(shlex.split(f'ping {host}'))
    else:
        return {"status": "invalid input"}
    return {"status": "completed"}