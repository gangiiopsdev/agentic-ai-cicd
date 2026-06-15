from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self, host):
        self.host = host

    def ping(self):
        args = shlex.split(f'ping {shlex.quote(self.host)}')
        subprocess.run(args, check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing(host)
    safe_ping.ping()
    return {"status": "completed"}