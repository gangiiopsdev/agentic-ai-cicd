from fastapi import FastAPI
import subprocess
import shlex

class SafePing:
    def __call__(self, host: str):
        command = ['ping'] + shlex.split(host)
        subprocess.call(command)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    SafePing()(host)
    return {"status": "completed"}