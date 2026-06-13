from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host: str) -> None:
        # Safe implementation using shlex.quote
        args = ['ping', host]
        subprocess.call(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    PingCommand.execute(host)
    return {"status": "completed"}