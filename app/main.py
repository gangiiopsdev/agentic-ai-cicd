from fastapi import FastAPI
import subprocess
class SafePinger:
    def __init__(self):
        self.allowed_hosts = ['example.com']

    def ping(self, host: str):
        if host in self.allowed_hosts:
            subprocess.call(['ping', host])
        else:
            raise ValueError('Host not allowed')

app = FastAPI()
pinger = SafePinger()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    pinger.ping(host)
    return {"status": "completed"}