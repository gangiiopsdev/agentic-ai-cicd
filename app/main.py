from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def safe_ping(host: str) -> bool:
    if not host or not host.strip():
        return False
    args = ['ping'] + shlex.split(host)
    try:
        result = subprocess.run(args, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=5)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f'Ping failed: {e.stderr}')
        return False

@app.get('/ping')
def ping(host: str):
    return {'result': safe_ping(host)}