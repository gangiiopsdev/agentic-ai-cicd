from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def ping(host: str):
        # Safer implementation using subprocess.run instead of shell=True
        subprocess.run(['ping', host], check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    SafePing.ping(host)
    return {"status": "completed"}