from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self):
        self.ping_command = 'ping'

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Safe implementation
    safe_host = subprocess.list2cmdline([host])
    result = subprocess.run([SafePing.ping_command, safe_host], capture_output=True, text=True)
    return {"status": "completed", "output": result.stdout}