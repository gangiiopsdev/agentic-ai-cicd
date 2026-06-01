from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.allowed_hosts = ['8.8.8.8', '127.0.0.1']

    def is_safe_host(self, host):
        return host in self.allowed_hosts

app = FastAPI()
safe_ping = SafePing()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if safe_ping.is_safe_host(host):
        subprocess.call(["ping", host])
    else:
        return {"error": "Invalid input"}

    return {"status": "completed"}