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
    try:
        result = subprocess.run(['ping', safe_host.host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}