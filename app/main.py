from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.safe_hosts = {'example.com'}

    def ping(self, host: str):
        if host in self.safe_hosts:
            args = ['ping', shlex.quote(host)]
            subprocess.run(args, check=True)
            return {"status": "completed"}
        else:
            raise ValueError('Host not allowed')

app = FastAPI()
safe_ping = SafePing()

@app.get("/ping")
def ping(host: str):
    return safe_ping.ping(host)