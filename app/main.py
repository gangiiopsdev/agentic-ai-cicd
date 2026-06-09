from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_command = ['ping', '-c', '1']

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    if not host:
        return {"error": "Host parameter is required"}
    result = subprocess.run(SafePing().ping_command + [host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}