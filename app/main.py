from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host):
        self.host = host
        self.command = ["ping", self.host]

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    subprocess.run(PingCommand(host).command, check=True)
    return {"status": "completed"}