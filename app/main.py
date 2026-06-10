from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def run_command(command: list):
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid host name")
    sanitized_host = quote(host)
    command = ["ping", "-c", "1", sanitized_host]
    return {"status": "completed", "output": run_command(command)}