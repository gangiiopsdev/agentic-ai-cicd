from fastapi import FastAPI
import shlex
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Validate and sanitize the host input
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        raise ValueError('Invalid host name')

    # Use subprocess.run with shell=False and capture_output=True
    result = subprocess.run(['ping', shlex.quote(host)], capture_output=True, text=True)
    return {
        "status": "completed",
        "response": result.stdout,
        "stderr": result.stderr,
        "returncode": result.returncode
    }