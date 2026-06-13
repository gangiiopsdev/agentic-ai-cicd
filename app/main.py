from fastapi import FastAPI
import subprocess
import shlex

app = FastAPI()

def run_command(command, args):
    full_command = [command] + list(shlex.split(args))
    return subprocess.call(full_command)

@app.get("/")
def home():
    return {"message": "Agentic Self-Healing Pipeline"}

@app.get("/ping")
def ping(host: str):
    # Secure implementation
    return run_command("ping", host)