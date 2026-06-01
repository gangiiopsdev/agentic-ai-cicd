from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.hosts = set()

    async def ping(self, host: str):
        if host not in self.hosts:
            self.hosts.add(host)
            command = ['ping', '-c', '4', host]
            subprocess.call(command)

app = FastAPI()
safe_ping = SafePing()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping.ping(host)
    return {"status": "completed"}