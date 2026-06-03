from fastapi import FastAPI
import subprocess
dfrom shlex import quote

app = FastAPI()

def escape_host(host):
    # Properly escape the host to prevent command injection
    return quote(host)

@app.get("/ping")
def ping(host: str):
    if not host.strip():
        raise ValueError("Host parameter is required and cannot be empty")
    escaped_host = escape_host(host)
    result = subprocess.run(['ping', '-c', '1', escaped_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}