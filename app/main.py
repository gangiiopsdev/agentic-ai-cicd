from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        result = subprocess.call(args)
        return result

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_route(host: str):
    return PingService.ping(host)