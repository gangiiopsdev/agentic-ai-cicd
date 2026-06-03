from fastapi import FastAPI
import subprocess
class PingResponse:
    def __init__(self, status):
        self.status = status

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run(['ping', host], check=True, timeout=10)
        return PingResponse(status="completed")
    except subprocess.CalledProcessError as e:
        return PingResponse(status=str(e))