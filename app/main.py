from fastapi import FastAPI
import subprocess
import shlex
import re

app = FastAPI()

def run_ping(host):
    try:
        # Validate host input to ensure it does not contain malicious content
        if not re.match(r'^[a-zA-Z0-9.-]+$', host):
            raise ValueError('Invalid host input')
        result = subprocess.run(shlex.split(f'ping {shlex.quote(host)}'), capture_output=True, text=True, check=True)
        return result.stdout
    except (subprocess.CalledProcessError, ValueError) as e:
        return str(e)

@app.get("/ping")
def ping(host: str):
    response = run_ping(host)
    return {"status": "completed", "response": response}