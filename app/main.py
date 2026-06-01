from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self):
        pass

    @staticmethod
def safe_ping(host: str):
        args = ['ping', host]
        subprocess.run(args, check=True)

global ping_command
ping_command = PingCommand()

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    ping_command.safe_ping(host)
    return {"status": "completed"}