from fastapi import FastAPI
import subprocess
import shlex
def safe_subprocess_call(command: str, *args):
    full_command = [command] + list(shlex.split(' '.join(args)))
    subprocess.call(full_command)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    safe_subprocess_call("ping", host)
    return {"status": "completed"}