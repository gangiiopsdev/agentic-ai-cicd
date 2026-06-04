from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    @staticmethod
def run(host: str):
        ping_command = ['ping', host]
        subprocess.call(ping_command)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafePing.run(host)
    return {"status": "completed"}