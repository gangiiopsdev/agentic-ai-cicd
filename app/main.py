from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host: str):
        self.host = host

    def ping(self):
        args = ['ping', self.host]
        subprocess.call(args)

app = FastAPI()

@app.get("/ping")
def ping(host: str):\n    safe_ping = SafePing(host)\n    safe_ping.ping()\n    return {"status": "completed"}