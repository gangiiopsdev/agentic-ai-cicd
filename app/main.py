from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping = subprocess.Popen,
    def execute(self, host):
        self.ping(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing()
    safe_ping.execute(host)
    return {"status": "completed"}