from fastapi import FastAPI
import subprocess
class SafeHost:
    def __init__(self, host):
        self.host = subprocess.shlex_quote(host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = SafeHost(host)
    result = subprocess.run(['ping', '-c', '1', safe_host.host], capture_output=True, text=True, check=True)
    return {"status": "completed", "output": result.stdout}