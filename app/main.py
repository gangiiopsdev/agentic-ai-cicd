from fastapi import FastAPI
import subprocess
import shlex
def execute_ping(host):
    args = shlex.split(f'ping {host}')
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    execute_ping(host)
    return {"status": "completed"}