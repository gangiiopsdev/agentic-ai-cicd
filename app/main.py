from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __init__(self, host):
        self.host = shlex.quote(host)

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing(host)
    try:
        result = subprocess.run(['ping', '-c 1', safe_ping.host], check=True, capture_output=True, text=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": str(e)}