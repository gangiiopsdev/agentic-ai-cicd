from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def safe_subprocess(command, args):
    full_command = [command] + list(shlex.split(args))
    subprocess.call(full_command)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_subprocess('ping', host)
    return {"status": "completed"}