from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host):
        # Safe implementation using Popen instead of call
        args = ['ping', host]
        subprocess.Popen(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    PingCommand.safe_ping(host)
    return {"status": "completed"}