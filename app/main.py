from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_command = 'ping'

    def ping(self, host: str):
        # Safe implementation using subprocess.call with shell=False
        subprocess.call([self.ping_command, host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing()
    safe_ping.ping(host)
    return {"status": "completed"}