from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.command = ['ping']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):\n    try:\n        subprocess.run(PingCommand().command + [host], check=True, timeout=5)\n    except subprocess.CalledProcessError as e:\n        return {"status": "error", "message": str(e)}\n    return {"status": "completed"}