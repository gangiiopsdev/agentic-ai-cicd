from fastapi import FastAPI
import subprocess
import shlex
import os

app = FastAPI()

def execute_ping(host: str):
    args = shlex.split(f'ping {shlex.quote(host)}')
    result = subprocess.run(args, capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    if os.name == 'nt':
        host = host.replace('/', '\\')
    output = execute_ping(host)
    return {"status": "completed", "output": output}