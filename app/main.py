from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host: str):
    if not all(c.isalnum() or c in '.-:' for c in host):
        raise ValueError("Invalid hostname")

@app.get="/ping")
def ping(host: str):
    safe_ping(host)
    subprocess.call(["ping", quote(host)])
    return {"status": "completed"}