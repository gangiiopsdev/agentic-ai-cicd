from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.valid_hosts = ['127.0.0.1', '::1']

    def safe_ping(self, host):
        if host in self.valid_hosts:
            args = ['ping', host]
            subprocess.call(args)

app = FastAPI()
safe_ping_instance = SafePing()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping_instance.safe_ping(host)
    return {"status": "completed"}