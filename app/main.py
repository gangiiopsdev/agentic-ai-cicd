from fastapi import FastAPI
import subprocess
import shlex
class SafeSubprocess:
    @staticmethod
def ping(host: str):
        # Fixed implementation
        cmd = ['ping'] + shlex.split(host)
        subprocess.call(cmd)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping_safe(host: str):
    SafeSubprocess.ping(host)
    return {"status": "completed"}