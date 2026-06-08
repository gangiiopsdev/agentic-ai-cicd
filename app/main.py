from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Enhanced security implementation with input validation
    if not re.match(r'^[a-zA-Z0-9.-]+$', host):
        return {"error": "Invalid host parameter"}
    result = subprocess.run(shlex.split(f'ping {host}'), capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}