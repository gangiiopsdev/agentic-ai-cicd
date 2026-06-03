from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        if host.isalnum():
            subprocess.call(["ping", host])
        else:
            raise ValueError("Invalid hostname")

app = FastAPI()

@app.get="/)")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafePing.safe_ping(host)
    return {"status": "completed"}