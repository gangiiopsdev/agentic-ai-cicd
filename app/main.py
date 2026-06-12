from fastapi import FastAPI
import shlex
import re

global host_var = "example.com"

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "invalid_host"}
    command_parts = shlex.split(f'ping {host}')
    subprocess.call(command_parts, shell=False)
    return {"status": "completed"}