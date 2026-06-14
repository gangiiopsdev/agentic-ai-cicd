from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host):
    # Validate and sanitize the input to prevent command injection
    if not host.isalnum():
        return "Invalid host name"
    try:
        result = subprocess.run(['ping', '-c 1', shlex.quote(host)], capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        return str(e)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Use shlex.quote to safely quote the host argument
    safe_host = shlex.quote(host)
    return {"status": safe_ping(safe_host)}