from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_subprocess(command: str, *args):
    cmd_parts = command.split(' ')
    for arg in args:
        cmd_parts.append(quote(arg))
    subprocess.run(cmd_parts, check=True)

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = quote(host)
    if not safe_host:
        raise ValueError("Invalid input")
    safe_subprocess('ping', safe_host)
    return {"status": "completed"}