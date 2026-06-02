from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell=False and proper validation of input
    if host.strip().isdigit() and len(host) <= 3:
        result = subprocess.run(shlex.split(f'ping -c 1 {host}'), capture_output=True, text=True)
        return result.stdout
    else:
        raise ValueError('Invalid host address')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    output = safe_ping(host)
    return {"status": "completed", "output": output}