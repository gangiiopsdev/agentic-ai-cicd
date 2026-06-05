from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    def ping_host(self, host):
        args = shlex.split(f'ping {host}')
        subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    service = PingService()
    service.ping_host(host)
    return {"status": "completed"}