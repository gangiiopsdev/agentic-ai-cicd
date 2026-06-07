from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def ping(host: str):
    try:
        # Use shlex to safely quote the host parameter
        command = ['ping'] + shlex.split(host)
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=5, shell=False)
        return {'status': 'completed', 'output': output.decode()}
    except subprocess.CalledProcessError as e:
        return {'status': 'failed', 'error': e.output.decode()}

@app.get("/ping")
def ping_endpoint(host: str):
    return ping(host)