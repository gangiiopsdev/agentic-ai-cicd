from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.safe_hosts = ['127.0.0.1', '::1']

    def is_safe_host(self, host):
        return host in self.safe_hosts

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    if not safe_ping.is_safe_host(host):
        return {"status": "failed", "error": "Host is not allowed."}
    try:
        result = subprocess.run(['ping', host], capture_output=True, text=True, check=True)
        return {"status": "completed", "output": result.stdout}
    except subprocess.CalledProcessError as e:
        return {"status": "failed", "error": e.stderr}