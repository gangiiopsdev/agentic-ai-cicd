from fastapi import FastAPI
import subprocess
import shlex

class PingService:
    @staticmethod
def ping(host: str):
        command = ['ping'] + shlex.split(host)
        return subprocess.run(command, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_endpoint(host: str):
    result = PingService.ping(host)
    return {"status": "completed", "output": result.stdout}