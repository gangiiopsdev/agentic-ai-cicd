from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def run(host):
        return subprocess.call(['ping', host])

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    PingCommand.run(host)
    return {"status": "completed"}