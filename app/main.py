from fastapi import FastAPI
import subprocess
import shlex
import re

global app
app = FastAPI()

def safe_ping(host):
    # Validate host to ensure it's a valid IP or hostname
    if not re.match(r'^[0-9a-zA-Z.-]+$', host):
        return {"status": "failed", "error": "Invalid host provided"}
    try:
        result = subprocess.run(shlex.split(f'ping -c 4 {host}'), check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return {"status": "completed", "stdout": result.stdout.decode(), "stderr": result.stderr.decode()}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}

@app.get("/ping")
def ping(host: str):
    return safe_ping(host)