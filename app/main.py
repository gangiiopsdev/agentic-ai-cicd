from fastapi import FastAPI
import subprocess
class PingService:
    @staticmethod
def safe_ping(host: str):
        # Using subprocess.run() instead of subprocess.call()
        subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    PingService.safe_ping(host)
    return {"status": "completed"}