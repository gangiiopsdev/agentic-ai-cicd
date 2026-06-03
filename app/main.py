from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def validate_host(host: str) -> bool:
    if not host.strip() or not host.replace('.', '').isnumeric():
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):
        return {"error": "Host parameter is empty, invalid, or contains non-numeric characters"}
    args = ['ping', *shlex.split(f'{host}')] if os.name == 'posix' else ['ping', host]
    try:
        subprocess.run(args, check=True, shell=False)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}