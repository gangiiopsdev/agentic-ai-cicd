from fastapi import FastAPI
import subprocess
class SafeHost:
    def __init__(self, host):
        self.host = subprocess.list2cmdline([host])

app = FastAPI()

@app.get("/ping")
def ping(host: str):
    safe_host = SafeHost(host)
    subprocess.call(['ping', safe_host.host])
    return {"status": "completed"}