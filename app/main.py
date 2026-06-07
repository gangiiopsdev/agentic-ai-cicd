from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    async def ping(self):
        await subprocess.run(['ping', self.host], capture_output=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing(host)
    await safe_ping.ping()
    return {"status": "completed"}