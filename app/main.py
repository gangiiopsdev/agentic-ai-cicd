from fastapi import FastAPI
import subprocess
import shlex

class PingCommand:
    @staticmethod
def execute(host: str):
        cmd = ['ping', host]
        subprocess.call(cmd, shell=False)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    PingCommand.execute(host)
    return {"status": "completed"}