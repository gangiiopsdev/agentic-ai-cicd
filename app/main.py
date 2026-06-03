from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def execute(host):
        # Safe implementation without shell=True
        subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    PingCommand.execute(host)
    return {"status": "completed"}