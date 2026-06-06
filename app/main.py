from fastapi import FastAPI
import subprocess
from shlex import quote
import os

app = FastAPI()

def safe_ping(host: str):
    cmd = ['ping', '-c', '1', quote(host)]
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()
    if process.returncode == 0:
        return {'status': 'completed', 'output': output}
    else:
        return {'status': 'error', 'error': error}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)