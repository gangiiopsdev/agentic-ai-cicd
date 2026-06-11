from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    def __init__(self):
        self.ping_command = ['ping', '-c', '4']

app = FastAPI()

@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    args = self.ping_command + shlex.split(host)
    subprocess.run(args, check=True, capture_output=True, text=True)
    return {"status": "completed"}