from fastapi import FastAPI
import subprocess
class PingCommand:
    def __init__(self, host: str):
        self.output, self.error = subprocess.run(['ping', host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    command = PingCommand(host)
    if command.error:
        return {"status": "failed", "error": command.error}
    return {"status": "completed", "output": command.output}