from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def call(host: str):
        return subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    result = PingCommand.call(host)
    return {"status": "completed", "output": result.stdout}