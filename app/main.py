from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def ping(host: str):
        return subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = PingService.ping(host)
    return {"status": "completed", "output": result.stdout}