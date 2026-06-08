from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    if not host.isalnum():
        raise ValueError("Invalid host name")
    sanitized_host = quote(host)
    result = subprocess.run(["ping", "-c", "1", sanitized_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}