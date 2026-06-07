from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def safe_ping(host):
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host input')
    try:
        output = subprocess.check_output(shlex.split(f'ping {host}'), stderr=subprocess.STDOUT, universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    return {"status": safe_ping(host)}