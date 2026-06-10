from fastapi import FastAPI
import subprocess
import re

app = FastAPI()

def sanitize_host(host: str) -> str:
    return ''.join(c for c in host if c.isalnum() or c in '-.')

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    # Validate input
    if not re.match(r'^[a-zA-Z0-9.-]+$', sanitized_host):
        return {"status": "failed", "error": "Invalid host name"}
    try:
        output = subprocess.check_output(['ping', sanitized_host], stderr=subprocess.STDOUT, text=True)
        return {"status": "completed", "output": output}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}