from fastapi import FastAPI
import subprocess
import re
import shlex

app = FastAPI()
cimport = subprocess.CalledProcessError

def validate_host(host):
    return re.match(r'^[a-zA-Z0-9]{1,}([.][a-zA-Z0-9]{1,})+$', host) is not None

@app.get("/ping")
def ping(host: str):
    if not validate_host(host):  # Validate host input to prevent injection attacks
        return {"status": "failed", "error": "Invalid host name"}

    try:
        result = subprocess.run(shlex.split(f'ping -c 1 {shlex.quote(host)}'), capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except cimport as e:
        return {"status": "failed", "error": e.stderr}