from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = host

    def ping(self):
        return subprocess.run(['ping', '-c', '1', self.host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing(host)
    result = safe_ping.ping()
    return {
        "status": "completed",
        "output": result.stdout,
        "stderr": result.stderr
    }