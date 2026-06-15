from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()

def safe_subprocess_call(command_parts):
    command_str = ' '.join(shlex.quote(part) for part in command_parts)
    return subprocess.call(command_str, shell=True)

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input
    if not re.match(r'^[a-zA-Z0-9]+$', host):
        raise ValueError("Invalid host name")
    command_parts = ['ping', host]
    return safe_subprocess_call(command_parts)