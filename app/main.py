from fastapi import FastAPI
import subprocess

app = FastAPI()

def run_ping(host):
    try:
        output = subprocess.check_output(['ping', host], stderr=subprocess.STDOUT, text=True)
        return output
    except subprocess.CalledProcessError as e:
        return str(e.output)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "error", "output": "Invalid host"}
    result = run_ping(host)
    return {"status": "completed", "output": result}

import re

def is_valid_host(host):
    pattern = r'^[a-zA-Z0-9.-]+$'
    return re.match(pattern, host) is not None