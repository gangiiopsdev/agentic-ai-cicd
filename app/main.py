from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def escape_host(host: str):
    return ''.join(ch for ch in host if ch.isalnum() or ch.isspace())

@app.get("/ping")
def ping(host: str):
    escaped_host = escape_host(host)
    subprocess.call(shlex.split(f"ping {escaped_host}"))
    return {"status": "completed"}