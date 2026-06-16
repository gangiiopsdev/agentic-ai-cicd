from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.allowed_hosts = {'google.com', 'example.com'}

    def ping(self, host: str):
        if host not in self.allowed_hosts:
            return {'status': 'error', 'message': 'Invalid host'}
        safe_host = shlex.quote(host)
        subprocess.call(['ping', safe_host], shell=False)
        return {"status": "completed"}

app = FastAPI()
safe_ping = SafePing()

@app.get("/")
def home():
    return {'message': 'Agentic Self-Healing Pipeline'}

@app.get("/ping")
def ping(host: str):
    return safe_ping.ping(host)