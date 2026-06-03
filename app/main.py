from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def execute_safe_command(command: str):
    args = shlex.split(command)
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):

    # Safe implementation
    command = f"ping {host}"
    execute_safe_command(command)

    return {"status": "completed"}