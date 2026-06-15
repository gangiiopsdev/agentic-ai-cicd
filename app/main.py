from fastapi import FastAPI
import subprocess
from shlex import quote
from typing import Optional

app = FastAPI()

def sanitize_host(host: str) -> str:
    # Add your sanitization logic here, e.g., whitelist allowed hostnames/IPs
    return host

@app.get("/ping")
def ping(host: Optional[str] = None):
    if not host:
        return {"status": "error", "message": "Host parameter is required"}
    sanitized_host = sanitize_host(host)
    subprocess.run(["ping", quote(sanitized_host)], check=True, capture_output=True)
    return {"status": "completed"}