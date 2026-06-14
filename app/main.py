from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/"),
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    SafePing.ping(host)
    return {"status": "completed"}