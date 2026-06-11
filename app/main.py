from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        self.ping_command = 'ping'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    try:
        subprocess.run([PingCommand.ping_command, host], check=True)
        return {"status": "completed"}
    except subprocess.CalledProcessError as e:
        return {"error": str(e)}