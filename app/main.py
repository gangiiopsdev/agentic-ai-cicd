from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host: str):
    # Ensure the host is a valid IP or hostname to avoid command injection
    if not host.isalnum() and '@' not in host:
        return "Invalid input"
    args = shlex.split(f"ping {host}")
    subprocess.call(args)

@app.get("/ping")
def ping(host: str):
    result = safe_ping(host)
    if isinstance(result, dict):
        return result
    else:
        return {"status": result}