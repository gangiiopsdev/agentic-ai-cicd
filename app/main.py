from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host: str):
    return ''.join(c for c in host if c.isalnum() or c in ('-', '.', '_', '+'))

app = FastAPI()

@app.get("/ping")
def ping(host: str):    safe_host = escape_host(host)
    subprocess.call(shlex.split(f"ping -c 1 {safe_host}"))  # Limit the number of pings to avoid denial-of-service attacks
    return {"status": "completed"}