from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def execute_ping(host):
        return subprocess.call(['ping', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    service = PingService()
    result = service.execute_ping(host)
    return {"status": "completed", "result": result}