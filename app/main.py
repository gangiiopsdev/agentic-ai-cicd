from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command, *args):
    args = shlex.split(command)
    return subprocess.call(args, shell=False)

@app.get("/ping")
def ping(host: str):
    command = f"ping {shlex.quote(host)}"
    result = run_command(command)
    return {"status": "completed", "result": result}