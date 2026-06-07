from fastapi import FastAPI
import subprocess
from shlex import quote
import re


def ping(host: str):
    try:
        output = subprocess.run(['ping', '-c', '1', quote(host)], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": output.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

app = FastAPI()

@app.get("/ping")
def ping_route(host: str):
    # Validate host input before passing it to the ping command
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"status": "failed", "error": "Invalid host input"}
    return ping(host)