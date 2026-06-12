from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def escape_shell_arg(arg):
    return arg.replace(';', '').replace('&', '').replace('|', '')

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize input to prevent command injection
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"error": "Invalid input"}, 400
    args = shlex.split(f'ping {escape_shell_arg(host)}')
    subprocess.run(args, check=True)
    return {"status": "completed"}