from fastapi import FastAPI
import subprocess
import shlex
class SafePinger:
    @staticmethod
def ping(host: str):
        args = ['ping', host]
        subprocess.run(args, check=True)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafePinger.ping(host)
    return {"status": "completed"}