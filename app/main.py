from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def safe_ping(host):
        # Construct the ping command safely using args instead of shell=True
        return ['ping', host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Call the safe_ping method with args instead of shell=True
    subprocess.call(PingCommand.safe_ping(host))
    return {"status": "completed"}