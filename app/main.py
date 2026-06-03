from fastapi import FastAPI
import subprocess
class PingCommand:
    @staticmethod
def run(host: str):
        args = ['ping', host]
        return subprocess.run(args, capture_output=True, text=True)
global ping_command
ping_command = PingCommand()

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host.isalnum():
        return {"status": "error", "output": "Invalid input"}
    result = ping_command.run(host)
    return {"status": "completed", "output": result.stdout}