from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def safe_ping(host):
        cmd = ['ping'] + shlex.split(host)
        subprocess.run(cmd, check=True, capture_output=True)
app = FastAPI()
@app.get="/"
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get="/ping"
def ping(host: str):
    SafePing.safe_ping(host)
    return {"status": "completed"}