from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        pass

    def ping(self, host: str):
        # Use subprocess.run with shell=False and list of arguments for safe execution
        subprocess.run(['ping', host], check=True)

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing()
    safe_ping.ping(host)
    return {"status": "completed"}