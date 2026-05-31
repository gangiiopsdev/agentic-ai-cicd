from fastapi import FastAPI
import subprocess
import shlex
class PingService:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/ping")
def ping_endpoint(host: str):
    return PingService.ping(host)

@app.get("")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}