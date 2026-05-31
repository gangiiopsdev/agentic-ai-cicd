from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def execute_ping(host: str):
        # Safer implementation
        subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafePing.execute_ping(host)
    return {"status": "completed"}