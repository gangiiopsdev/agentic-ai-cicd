from fastapi import FastAPI
import subprocess
import shlex

class PingHost:
    def __init__(self, host: str):
        self.host = shlex.quote(host)

    def ping(self):
        # Secure implementation
        subprocess.run(['ping', self.host], check=True)

app = FastAPI()

@app.get("/ping")
def ping_secure(host: str):
    ping_host = PingHost(host)
    ping_host.ping()
    return {"status": "completed"}