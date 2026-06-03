from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def execute_ping(host):
    try:
        host = shlex.quote(host)
        result = subprocess.run(['ping', '-c', '1', host], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    return execute_ping(host)