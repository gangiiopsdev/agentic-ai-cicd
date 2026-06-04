from fastapi import FastAPI
import subprocess
import shlex
class SafePinger:
    def __init__(self):
        pass

    def ping(self, host: str):
        args = shlex.split(f"ping {host}")
        subprocess.run(args)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    pinger = SafePinger()
    pinger.ping(host)
    return {"status": "completed"}