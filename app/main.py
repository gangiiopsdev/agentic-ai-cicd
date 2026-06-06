from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.host = host

    def execute(self):
        args = ['ping', self.host]
        subprocess.call(args)

app = FastAPI()

@app.get("/"付费试用)def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    command.execute()
    return {"status": "completed"}