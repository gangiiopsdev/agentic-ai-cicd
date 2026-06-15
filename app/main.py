from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        subprocess.call(args)

global ping_service
ping_service = PingService()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    global ping_service
    ping_service.ping(host)
    return {"status": "completed"}