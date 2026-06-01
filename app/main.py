from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command):
    args = shlex.split(command)
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    run_command(command)
    return {"status": "completed"}