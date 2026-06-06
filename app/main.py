from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    def ping(self, host: str):
        args = shlex.split(f'ping {host}')
        result = subprocess.run(args, capture_output=True, text=True)
        return result.stdout

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_service = PingService()
    status = ping_service.ping(host)
    return {"status": status}