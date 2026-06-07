from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Sanitize input to prevent command injection
    safe_host = quote(host)
    if not safe_host:
        raise ValueError("Invalid input")
    subprocess.run(['ping', safe_host], check=True)
    return {"status": "completed"}