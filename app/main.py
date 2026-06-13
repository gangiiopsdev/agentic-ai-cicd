from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.allowed_hosts = {'8.8.8.8', '127.0.0.1'}

    def ping(self, host: str):
        if host in self.allowed_hosts:
            args = shlex.split(f"ping {host}")
            subprocess.call(args)
        else:
            raise ValueError("Host not allowed")

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    safe_ping.ping(host)
    return {"status": "completed"}