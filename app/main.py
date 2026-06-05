from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.hosts = set()
    def ping(self, host: str):
        if host not in self.hosts:
            self.hosts.add(host)
            args = shlex.split(f"ping {host}")
            subprocess.run(args, check=True)

app = FastAPI()
safe_ping_instance = SafePing()
@app.get("/ping")
def ping(host: str):
    return safe_ping_instance.ping(host)