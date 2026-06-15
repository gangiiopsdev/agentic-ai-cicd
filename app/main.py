from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.ping_command = 'ping'

    def ping(self, host):
        args = [self.ping_command, host]
        subprocess.call(shlex.split(args))

app = FastAPI()

 cp = SafePing()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "error", "message": "Invalid input"}
    cp.ping(host)
    return {"status": "completed"}