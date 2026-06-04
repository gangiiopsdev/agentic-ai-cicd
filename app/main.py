from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, command):
        self.command = command

    def safe_execute(self, host):
        full_command = [self.command, host]
        subprocess.call(full_command)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing("ping")
    safe_ping.safe_execute(host)
    return {"status": "completed"}