from fastapi import FastAPI
import subprocess
import re
import os

app = FastAPI()

def is_valid_host(host):
    return re.match(r'^[a-zA-Z0-9.-]+$', host)

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        return {"status": "invalid input"}
    args = ['ping', '-c', '4', os.path.abspath(host)]  # Use absolute path to prevent directory traversal
    subprocess.run(args, check=True)
    return {"status": "completed"}