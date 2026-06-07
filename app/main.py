from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __call__(self, host):
        ping_command = ['ping'] + shlex.split(host)
        return subprocess.run(ping_command, capture_output=True, text=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_ping = SafePing()
    result = safe_ping(host)
    return {"status": "completed", "output": result.stdout}