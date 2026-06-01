from fastapi import FastAPI
import subprocess
from shlex import quote
class SafeHost:
    def __init__(self, host):
        self.host = quote(host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = SafeHost(host)
    subprocess.run(['ping', safe_host.host], check=True)
    return {"status": "completed"}