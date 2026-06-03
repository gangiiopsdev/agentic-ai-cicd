from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_ping(host):
    # Validate and sanitize the host input to prevent injection attacks
    if not host or len(host) > 255 or ' ' in host:
        raise ValueError("Invalid host")
    result = subprocess.run(['ping'] + shlex.split(host), capture_output=True, text=True)
    return result.stdout

@app.get("/ping")
def ping(host: str):
    status = safe_ping(host)
    return {"status": "completed", "output": status}