from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, host: str, *args, **kwargs):
        super().__init__(['ping', host], *args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    command.wait()
    return {"status": "completed"}