from fastapi import FastAPI
import subprocess
import shlex
import re

global app = FastAPI()

def safe_subprocess(command: str, args: list) -> None:
    full_command = [command] + shlex.split(' '.join(args))
    subprocess.run(full_command, check=True)

@app.get("/ping")
def ping(host: str):
    # Safe implementation with input validation
    if not re.match(r'^[a-zA-Z0-9.-]+\.com$', host):
        return {"error": "Invalid host"}
    safe_subprocess("ping", [host])
    return {"status": "completed"}