from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def sanitize_host(host):
    return ''.join(c for c in host if c.isalnum() and c.isprintable())

@app.get("/ping")
def ping(host: str):
    sanitized_host = sanitize_host(host)
    if not sanitized_host:
        return {"error": "Invalid input"}
    subprocess.run([quote('ping'), quote(sanitized_host)], check=True, capture_output=True)
    return {"status": "completed"}