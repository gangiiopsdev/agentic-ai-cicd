from fastapi import FastAPI
import subprocess
class SafePinger:
    def __init__(self):
        self.ping_cmd = ['ping', '-c', '1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "error", "message": "Invalid hostname"}
    try:
        subprocess.call(SafePinger.ping_cmd + [host])
        return {"status": "completed"}
    except Exception as e:
        return {"status": "error", "message": str(e)}