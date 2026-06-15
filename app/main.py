from fastapi import FastAPI
import subprocess
import shlex
class SafePing:
    @staticmethod
def ping(host: str):
        safe_host = shlex.quote(host)
        args = ['ping', safe_host]
        subprocess.run(args, check=True)
app = FastAPI()
@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}
@app.get("/ping")
def ping(host: str):
    SafePing.ping(host)
    return {"status": "completed"}