from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_command(command, args):
    full_command = [command] + shlex.split(args)
    subprocess.call(full_command)

@app.get("/ping")
def ping(host: str):
    execute_command("ping", host)

    return {"status": "completed"}