from fastapi import FastAPI
import subprocess
class PingCommand(subprocess.Popen):
    def __init__(self, host: str, *args, **kwargs):
        super().__init__(f'ping {host}', shell=False, *args, **kwargs)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    if command.wait() == 0:
        return {"status": "completed", "result": True}
    else:
        return {"status": "failed", "result": False}