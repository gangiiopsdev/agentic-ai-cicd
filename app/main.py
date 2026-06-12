from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        if not host.isalnum():
            raise ValueError('Invalid host')
        subprocess.call(['ping', host])
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    SafePing.safe_ping(host)
    return {"status": "completed"}