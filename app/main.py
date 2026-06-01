from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    # Fixed implementation using subprocess.run for better security
    sanitized_host = host.strip().replace(' ', '_')
    subprocess.run(["ping", quote(sanitized_host)], check=True)
    return {"status": "completed"}