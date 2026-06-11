from fastapi import FastAPI
import shlex
import subprocess

class SafePing:
    def __call__(self, host: str):
        args = ['ping', shlex.quote(host)]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get(")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_pinger = SafePing()
    safe_pinger(host)
    return {"status": "completed"}