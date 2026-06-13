from fastapi import FastAPI
import subprocess
import shlex
class PingWrapper:
    @staticmethod
def ping(host: str):
        cmd = ['ping'] + shlex.split(host)
        subprocess.run(cmd, check=True, capture_output=True, text=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    PingWrapper.ping(host)
    return {"status": "completed"}