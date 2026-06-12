from fastapi import FastAPI
import subprocess
import shlex
def run_command(command):
    args = shlex.split(command)
    subprocess.run(args, check=True)
app = FastAPI()
@app.get("/ping")
def ping(host: str):
    command = f"ping {host}"
    run_command(command)
    return {"status": "completed"}