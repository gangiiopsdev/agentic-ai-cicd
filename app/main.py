from fastapi import FastAPI
import subprocess
class SafePing:
    @staticmethod
def safe_ping(host):
        # Use subprocess.run instead of subprocess.call and avoid shell=True
        return subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Use the safe version of ping
    result = SafePing.safe_ping(host)
    return {"status": "completed", "output": result.stdout}