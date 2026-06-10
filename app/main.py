from fastapi import FastAPI
import subprocess
import shlex
def safe_ping(host: str):
    args = shlex.split(f"ping {host}")
    subprocess.call(args)
app = FastAPI()
@app.get("/ping")
def ping(host: str):  # Safe implementation
    safe_ping(shlex.quote(host))  # Sanitize input with shlex.quote
    return {"status": "completed"}