from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_command(command_parts):
    return shlex.split(' '.join(command_parts))

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using shlex.split for safe command construction
    command_parts = ['ping', host]
    command = safe_command(command_parts)
    subprocess.call(command)

    return {"status": "completed"}