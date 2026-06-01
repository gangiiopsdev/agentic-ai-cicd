from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command_parts):
    subprocess.call(command_parts, shell=False)

@app.get("/ping")
def ping(host: str):
    # Safe implementation using shlex to escape command parts
    command_parts = shlex.split(f'ping {host}')
    safe_subprocess(command_parts)
    return {"status": "completed"}