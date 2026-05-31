from fastapi import FastAPI
import subprocess
import shlex
from typing import List

app = FastAPI()

def ping(host: str):
    try:
        args = ['ping', '-c', '1'] + [arg for arg in host.split() if arg.strip()]  # Validate and sanitize input
        result = subprocess.run(args, capture_output=True, text=True, check=True)
        return {'status': 'completed', 'output': result.stdout}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.stderr}

@app.get("/ping")
def ping_route(host: str):
    return ping(host)