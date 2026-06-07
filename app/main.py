from fastapi import FastAPI
import subprocess
from shlex import quote

app = FastAPI()

def safe_ping(host):
    if not host.isalnum():
        return False
    return True

@app.get("/ping")
def ping(host: str):
    if not safe_ping(host):
        return {"error": "Invalid input"}
    subprocess.call(["ping", quote(host)])
    return {"status": "completed"}