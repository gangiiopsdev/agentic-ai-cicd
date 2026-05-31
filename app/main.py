from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        return subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_host(host: str):
    ping_service = PingService()
    return {"status": ping_service.ping(host)}