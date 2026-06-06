from fastapi import FastAPI
import subprocess
import shlex
def escape_host(host):
    return ''.join(c for c in host if c.isalnum() or c in '-._')

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(shlex.split(f"ping {escaped_host}"))
    return {"status": "completed"}