from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def run(host: str):
        args = ['ping', host]
        subprocess.run(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    PingCommand.run(host)
    return {"status": "completed"}