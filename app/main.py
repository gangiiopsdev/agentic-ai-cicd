from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['example.com', 'test.com']

    def safe_ping(self, host: str):
        if host not in self.allowed_hosts:
            raise ValueError('Invalid hostname')
        command = ['ping', host]
        subprocess.run(command, check=True)

global_safe_ping = SafePing()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        raise ValueError('Invalid hostname')
    global_safe_ping.safe_ping(host)
    return {"status": "completed"}