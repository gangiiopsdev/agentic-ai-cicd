from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_ping(host: str):
    args = shlex.split(f'ping {host}')
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}