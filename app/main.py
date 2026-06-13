from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def is_valid_host(host):
    pattern = re.compile(r'^[a-zA-Z0-9]{1,255}$')
    return bool(pattern.match(host))

@app.get("/ping")
def ping(host: str):
    if not is_valid_host(host):
        raise ValueError("Invalid host name")
    # Validate the input further to ensure it's safe for subprocess execution
    if '&&' in host or ';' in host or '|' in host:
        raise ValueError("Input contains unsafe characters")
    command = ["ping", shlex.quote(host)]
    result = subprocess.run(command, capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}