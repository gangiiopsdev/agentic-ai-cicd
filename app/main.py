from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['127.0.0.1', '::1']

    def safe_ping(self, host: str):
        if host in self.allowed_hosts:
            args = ["ping", shlex.quote(host)]
            subprocess.run(args, check=True)
        else:
            raise ValueError('Host not allowed')
global_safe_ping = SafePing()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global_safe_ping.safe_ping(host)
    return {"status": "completed"}