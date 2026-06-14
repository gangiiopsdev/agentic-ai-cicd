from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.hosts = set()

    async def ping(self, host: str):
        if host not in self.hosts:
            self.hosts.add(host)
            args = ['ping', '-c', '1', shlex.quote(host)]
            subprocess.run(args, check=True)

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    safe_ping.ping(host)
    return {"status": "completed"}