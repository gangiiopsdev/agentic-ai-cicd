from fastapi import FastAPI
import subprocess
def safe_ping(host: str):
    # Ensure the host is sanitized or validated before passing it to subprocess
    if not all(c.isalnum() or c in [".", "-"] for c in host):
        raise ValueError("Invalid host name")
    subprocess.call(["ping", host])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping(host)
    return {"status": "completed"}