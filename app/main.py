from fastapi import FastAPI
import subprocess
import shlex

global app = FastAPI()

def home():
    return {"message": "Agentic Self-Healing Pipeline"}

def ping(host: str):
    # Safe implementation
    args = ['ping', *shlex.split(host)]
    subprocess.call(args)

app.get("/ping")(ping)