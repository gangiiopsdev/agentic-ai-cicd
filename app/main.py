from fastapi import FastAPI
import subprocess
class SafePing:
    def __init__(self, host):
        self.host = subprocess.shlex_quote(host)

    def execute(self):
        return subprocess.run(['ping', self.host], capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing(host)
    result = safe_ping.execute()
    return {
        "status": "completed",
        "exit_code": result.returncode,
        "stdout": result.stdout,
        "stderr": result.stderr
    }