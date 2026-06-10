from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host: str):
        return subprocess.run(['ping', host], capture_output=True, text=True)

global_safe_ping = SafePing()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = global_safe_ping.safe_ping(host)
    return {"status": "completed", "output": result.stdout}