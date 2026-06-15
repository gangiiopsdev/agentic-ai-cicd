from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    # Safe implementation using subprocess.run with shell injection and argument splitting
    args = ['ping'] + shlex.split(host)
    subprocess.run(args, check=True, capture_output=True)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = shlex.quote(host)  # Ensure the host input is properly quoted for shlex
    safe_ping(escaped_host)
    return {"status": "completed"}